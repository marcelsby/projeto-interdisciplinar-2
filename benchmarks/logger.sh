#!/bin/sh

function getLogFileName { 
    read -p "Digite um nome para identificar seu arquivo de log (PADRÃO: benchmark-log):" logfileName
    logfileName=${pid:-"./statistics/benchmark-log"}
    logfileExtension=".txt"
    logfileParsed="$logfileName$logfileExtension"
    echo $logfileParsed
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
    local name=$(ps -q $pid -o comm=)
    echo "PID: $pid"
    echo "Nome: $name"
    echo "Data do teste: $(date +"%d-%m-%Y")"
    printf "\n"
    echo "$(ps aux | sed -n 1p | awk '{ print "Timestamp "$3" RAM" }')"
}

function getRamInMB () {
	local ramUsage=$(bc <<< "$totalRam * $ramUsagePercent / 100")
	return $ramUsage
}

function getLog () {
    totalRam=$(free -m | sed -n 2p | awk '{ print $2 }')
    local loopCondition=$(ps u -p "$pid" | wc -l)

    while [ $loopCondition == 2 ]
    do
        loopCondition=$(ps u -p "$pid" | wc -l)

        local ramUsagePercent=$(ps u -p "$pid" | sed -n 2p | awk '{ print $4 }')
        local timestamp=$(date +"%T")
        local cpuUsagePercent=$(ps u -p "$pid" | sed -n 2p | awk '{ print $3 }')

        getRamInMB
        local ramUsage="$?M" 

        echo "$timestamp $cpuUsagePercent $ramUsage" | column -t >> $logfileParsed
        sleep 3s    
    done
}

getLogFileName
getPid
getHeader > $logfileParsed
getLog

printf "Concluído com sucesso!\n"
