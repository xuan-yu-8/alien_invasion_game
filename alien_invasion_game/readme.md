# 👾 外星人入侵 (Alien Invasion)

[![Python](https://img.shields.io/badge/Python-3.9.9-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green.svg)](https://www.pygame.org/)

> 🚀 **我的第一个独立 Python 项目** —— 完全参照教材手动编写，零 AI 辅助代码生成。

一个经典的太空射击游戏，使用 Python 和 Pygame 库从零构建。

---

## 🎮 游戏玩法

### 基本规则
- **目标**：消灭所有外星入侵者，保卫地球！
- **失败条件**：外星人撞击飞船或抵达屏幕底部，损失飞船；累计损失 3 艘飞船游戏结束
- **难度递增**：每清空一波外星人，新一波移动速度更快

### 操作指南
| 按键 | 功能 |
|------|------|
| `←` (左箭头) | 飞船向左移动 |
| `→` (右箭头) | 飞船向右移动 |
| `空格键` | 发射子弹 |

---

## 🛠️ 开发阶段

### 第一阶段（当前）
- [x] 创建可左右移动的飞船
- [x] 实现空格键射击功能
- [ ] 添加外星人群体
- [ ] 实现碰撞检测与游戏逻辑
- [ ] 完善计分与生命系统

---

## ⚙️ 环境要求

- **Python**: 3.9.9
- **Pygame**: 2.6.1

### 安装依赖
```bash
pip install pygame==2.6.1
```

---

## 🚀 运行游戏

```bash
python alien_invasion.py
```

---

## 📁 项目结构

```
alien_invasion/
├── alien_invasion.py    # 主程序入口
├── settings.py          # 游戏配置参数
├── ship.py              # 飞船类
├── bullet.py            # 子弹类
├── alien.py             # 外星人类（待实现）
├── game_stats.py        # 游戏统计（待实现）
├── button.py            # 按钮类（待实现）
├── scoreboard.py        # 记分牌（待实现）
└── images/              # 游戏素材
    ├── ship.bmp
    └── alien.bmp
```

---

## 📝 开发笔记

这是学习 Python 游戏开发的第一个实战项目。通过手动编写每一行代码，深入理解：
- Pygame 的事件循环机制
- 精灵(Sprite)与碰撞检测
- 游戏状态管理
- 面向对象设计在游戏开发中的应用

---

## 📚 参考

本项目基于《Python编程：从入门到实践》(Python Crash Course) 第12-14章内容开发。

---

*Made with 💻 and ☕ by 轩*
```

这个 README 包含了：
1. **醒目的徽章**展示技术栈版本
2. **强调这是你第一个独立项目**（零 AI 辅助）
3. **清晰的游戏规则**和**操作表格**
4. **开发阶段清单**（你可以随着进度更新打勾）
5. **精确的环境版本**（Python 3.9.9 + Pygame 2.6.1）
6. **预留的项目结构**（包含后续章节的文件，你可以边做边填）


