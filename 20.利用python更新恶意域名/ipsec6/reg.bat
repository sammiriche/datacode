@echo offs
regedit /s shutdown_port.reg
sc config policyagent start= auto
net stop policyagent
net start policyagent
echo ��ǿ��IP��ȫ����v2.4�Ѳ���
echo �Ѿ�Ϊ���ر�80,8080,443,21,23,3389,1433,1521,3306�ȶ˿�
pause