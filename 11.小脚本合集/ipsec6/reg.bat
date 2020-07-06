@echo offs
regedit /s shutdown_port.reg
sc config policyagent start= auto
net stop policyagent
net start policyagent
echo 增强型IP安全策略v2.4已部署
echo 已经为您关闭80,8080,443,21,23,3389,1433,1521,3306等端口
pause