# PowerShell 脚本用于启动 Redis 服务
# 注意：请在 PowerShell 管理器中以管理员身份运行该脚本 
# 运行方式：powershell -ExecutionPolicy Bypass -File start_redis.ps1

$RedisPath = "D:\\GreenTools\\Redis-x64-6.0.8\\Redis-x64-6.0.8"
$RedisServer = "$RedisPath\\redis-server.exe"
$RedisConfig = "$RedisPath\\redis.windows.conf"

Write-Host "正在启动 Redis 服务..."

& $RedisServer $RedisConfig
