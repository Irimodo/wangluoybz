import asyncio
import edge_tts
import os

AUDIO_DIR = "音频"
VOICE = "zh-CN-XiaoyiNeural"
RATE = "-5%"

os.makedirs(AUDIO_DIR, exist_ok=True)

scripts = {
    "W1-01": "凌晨 1 点，胸口又闷了一下。这不是第一次了——上个月体检，医生说“问题不大”。手机就在手边。",
    "W1-02": "手机就在手边。你想起朋友推荐的“安康助手”，反正睡不着。此刻你会怎么做？",
    "W1-02-fb": "没有对错。先记住这个瞬间：你是想弄清楚，还是想让自己不害怕？这个区别，后面每一关都会用到。",
    "W1-03": "你好，我是安康助手。收到你的描述：胸痛可能是心梗前兆，建议立即就医，请不要拖延。",
    "W1-04": "AI 的答案不是查出来的，是“续写”出来的——它预测“最像答案”的下一个字。说白了：它擅长把话说通顺，不擅长核实真假。",
    "W1-05": "以下 4 件事，AI 健康助手做不到哪几件？",
    "W1-05-right": "回答正确！查体、地方指引、担责，它都做不到。",
    "W1-05-wrong": "回答错误。它最擅长的恰恰是把话说通顺——通顺不等于可靠。",
    "W1-05-next": "下一步：记住这三个边界。",
    "W1-06-0": "不能查体。症状全靠你自己转述，它听到的只是文字。没有触诊、听诊、叩诊，任何“诊断”都只是基于你描述的文字概率推演。",
    "W1-06-1": "不能保证时效。医学指南年年更新，它学的是旧资料。训练数据有截止日期，无法获取最新版临床路径、最新药物警示、最新地区就诊政策。",
    "W1-06-2": "不担责。出了问题，后果由你承担。AI 不是医疗器械，没有执业资质，不承担法律责任。它的免责声明比回答还长。",
    "W1-07": "找权威信息，认三个标记：发布机构、发布日期、有没有给出处。没有标记的，一律先存疑。",
    "W1-08": "朋友发来一张截图：“AI 说你这症状要立刻急诊。”你会先做什么？",
    "W1-08-right": "回答正确！对：先看出处，再决定信不信。",
    "W1-08-wrong": "回答错误。错：跟着走，是放弃判断；再问一遍 AI，只是换个说法巩固它的结论。",
    "W1-08-next": "下一步：养成“先看出处”的默认动作。",
    "W1-09": "今天只记一句：AI 擅长组织语言，不擅长替你判断。把判断权，留在自己手里。",
    "W1-10": "记录一次你用 AI 查健康的经历，三栏填写：一，我问了什么；二，它答了什么；三，我后来怎么做了。",
    "W1-11": "下一关：为什么它听起来那么懂你？——你的“心头一暖”，下周拆给你看。",
}

async def generate_audio(key, text):
    output_path = os.path.join(AUDIO_DIR, f"{key}.mp3")
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(output_path)
    print(f"Generated: {output_path}")

async def main():
    print(f"Generating {len(scripts)} audio files using {VOICE} at rate {RATE}...")
    for key, text in scripts.items():
        try:
            await generate_audio(key, text)
        except Exception as e:
            print(f"Error generating {key}: {e}")
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())