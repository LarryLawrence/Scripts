ROM�����ء���ѹ�ʹ���:

1.getZipTimeDelayVer ������ȡ'http://www.romzj.com/rom/*.htm'ҳ���ϵ�ROM�ĵ�ַ����׽���1�롣������浽out.txt��
for number in range(32000, 32999+1):��仰�������޸�*.htm�����е�*��Χ���Ѿ������˵ķ�Χ�������ƶ�Ӳ�����ҵ���

2.dd.py ��������ץ���ĵ�ַ����Ҫ������ĵ�ַ���������ֶ�������[]��""����ȥ��������ȥ�������档Ȼ����dd.py������ļ��������ˣ�line122����line129���Կ������شӵڼ��еĵ�ַ��ʼ�����ڼ��н�����
��ʱ��ROM���غ��ˡ�

3.unzip.py ���԰�*.zip�е�boot.img��build.prop(������ڵĻ�)��ѹ���ŵ���ǰĿ¼��temp�ļ����¡�
����֮ǰ�������޸�zip���ڵ�·��filepath���Լ�zip�����Ƶķ�Χcount������300.zip��ʼ����399.zip��������ôcount�͸�ֵ300��399��

4.�����Ҫ�������������ȡkernel img,��ȡlinux version, build version,��ȡoffset����Ҫ������temp�е������ļ��п���linux��
Ȼ��ֱ���splitandwalk.sh ,AddLinux_and_BuildVersion.sh�� AddTestInfo.sh�������С�test���ļ���Ľ�������RESULT.TXT��������Ҫ������ļ����õ���Ӧλ�á���


���⻹��Щûʲô���õģ�����Min_N_Max.py���ڻ�ȡ������excel��6�����ݡ�


zhihuan.lc Aug 2015