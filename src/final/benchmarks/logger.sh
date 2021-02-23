#!/bin/sh

function getLogFileName { 
    read -p "Digite um nome para identificar seu arquivo de log (PADRÃO: benchmark-log): " logfileName
    logfileName=${logfileName:-"benchmark-log"}
    logfileExtension=".csv"
    logfileParsed="./results/$logfileName$logfileExtension"
    echo "Salvando como: $logfileParsed"
}

function getPid () {
    read -p "Digite o PID do processo que deseja monitorar: " pid
    pid=${pid:-0}

    if [ $pid == 0 ]
    then
        echo "Por favor, insira um PID válido. Saindo..."
        exit 
    fi
}

function getHeader () {
    pname=$(ps -q $pid -o comm=)
    echo "PID,$pid,"
    echo "Nome,$pname,"
    echo "Data do teste,$(date +"%d-%m-%Y"),"
    printf "\n"
    echo "$(ps aux | sed -n 1p | awk '{ print "Timestamp,"$3",RAM," }')"
}

function showInfo () {
    clear
    echo "PID: $pid"
    echo "Nome do processo: $pname"
    echo "Para finalizar o monitoramento pressione Ctrl + C ou aguarde o processo finalizar."
}

function getLog () {
    local loopCondition=$(ps u -p "$pid" | wc -l)

    while [ $loopCondition == 2 ]
    do
	local rssMem=$(ps -q $pid -o rss | sed -n 2p)
        local timestamp=$(date +"%T")
	local procRamUsageMB=$(bc <<< "$rssMem / 1000")
        local procCpuUsage=$(ps u -p "$pid" | sed -n 2p | awk '{ print $3 }')

        echo "$timestamp,$procCpuUsage,$procRamUsageMB," >> $logfileParsed

        sleep 3s    

        loopCondition=$(ps u -p "$pid" | wc -l)
    done
}

getLogFileName
getPid
getHeader > $logfileParsed
showInfo
getLog

# Deleta a última linha do arquivo de saída
sed -i '$d' $logfileParsed

printf "Concluído com sucesso!\n"
printf "Arquivo de saída: $logfileParsed\n"
