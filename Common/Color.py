# Color Palette for a Simple Game (Expanded)

# --- Original Palette ---
# 1. #61c0bf  -> (97, 192, 191)
TEAL_GREEN = (97, 192, 191)
# 英文名: Teal Green / Medium Aquamarine / Dusty Turquoise
# 配色建议:
# - 主要的UI元素颜色: 如按钮、图标、进度条等，因为它既醒目又不过于刺眼。
# - 次要背景或区域划分: 如果主要背景是更浅的颜色，这个颜色可以用来区分不同的功能区域。
# - 游戏中的“中性”或“功能性”对象: 例如平台、可交互的机关等。
# - 偏冷色调的自然元素：如平静的水面、远山等。

# 2. #bbded6  -> (187, 222, 214)
PALE_MINT = (187, 222, 214)
# 英文名: Pale Mint / Light Seafoam Green / Celadon Tint
# 配色建议:
# - 主要的游戏背景色: 这是一个非常柔和且令人平静的颜色，适合作为大面积背景，不会分散玩家注意力。
# - UI面板的背景: 例如设置菜单、得分板的背景。
# - 温和的地面或植被: 如果游戏场景简单，可以用作草地或地面的底色。
# - “安全区”或“休息区”的提示色。

# 3. #fae3d9  -> (250, 227, 217)
LIGHT_PEACH = (250, 227, 217)
# 英文名: Light Peach / Pale Apricot / Very Light Pinkish Beige
# 配色建议:
# - 辅助背景色或高光区域: 如果PALE_MINT是主背景，这个颜色可以用于需要略微提亮的区域。
# - 文本框或提示框的背景: 尤其是当文字颜色较深时，能提供良好的对比度。
# - 非常柔和的UI元素: 如被选中的选项背景、分割线等。
# - 温暖、友好的氛围营造色。

# 4. #ffb6b9  -> (255, 182, 185)
SOFT_PINK = (255, 182, 185)
# 英文名: Soft Pink / Light Coral Pink / Baby Pink
# 配色建议:
# - 重要的提示或强调色: 如生命值、爱心、重要的可收集物品、警告（但不是非常强烈的警告）。
# - 玩家角色或可爱的NPC颜色: 能让角色显得突出且友好。
# - UI中的“积极”反馈: 如“成功”、“获得奖励”等提示的颜色。
# - 装饰性元素或花朵等。

# --- New In-Between and Complementary Soft Colors ---

# 5. #89c9c7 -> (137, 201, 199) - (介于 TEAL_GREEN 和 PALE_MINT 之间，更亮一些的青色)
LIGHT_AQUA = (137, 201, 199)
# 英文名: Light Aqua / Soft Cyan / Pale Turquoise
# 配色建议:
# - 次要UI元素: 当TEAL_GREEN作为主要UI色时，这个颜色可以用于其悬停状态或次级按钮。
# - 温和的提示信息背景: 不如SOFT_PINK那么强调，但仍能引起注意。
# - 水体或天空的柔和过渡色。
# - 装饰性的图案或边框。

# 6. #d8ebe4 -> (216, 235, 228) - (比 PALE_MINT 更浅，更接近白色的薄荷色)
VERY_PALE_MINT = (216, 235, 228)
# 英文名: Very Pale Mint / Almost White Mint / Misty Jade
# 配色建议:
# - 极浅的背景: 如果PALE_MINT还不够浅，或者需要背景有细微的层次感。
# - UI中的分隔线或非常细微的区域划分。
# - "幽灵"或半透明效果的底色。
# - 营造非常干净、空灵的氛围。

# 7. #fceee9 -> (252, 238, 233) - (介于 LIGHT_PEACH 和 PALE_MINT 之间，更偏暖的极浅色)
PEACH_BLUSH = (252, 238, 233)
# 英文名: Peach Blush / Ultra Light Apricot / Faint Rosy Beige
# 配色建议:
# - 作为LIGHT_PEACH的更亮版本，用于高光或需要更细腻过渡的背景。
# - 非常柔和的文本框背景，搭配深色文字。
# - UI中非激活状态的元素，或需要“呼吸感”的区域。
# - 温暖色调的云朵或光晕效果。

# 8. #ffd9d9 -> (255, 217, 217) - (比 SOFT_PINK 更浅更柔和的粉色)
PALE_ROSE = (255, 217, 217)
# 英文名: Pale Rose / Very Soft Pink / Light Pink Frost
# 配色建议:
# - 温和的积极反馈: 比SOFT_PINK更不具侵略性，适合微妙的成功提示。
# - 装饰性元素，如花瓣、柔光。
# - 女性化或可爱角色的辅助色彩。
# - UI中需要轻微强调的非关键信息。

# 9. #a5b8b7 -> (165, 184, 183) - (一个柔和的灰绿色/灰蓝色，作为中性过渡)
DUSTY_CYAN_GRAY = (165, 184, 183)
# 英文名: Dusty Cyan Gray / Soft Slate Teal / Muted Sage
# 配色建议:
# - 中性背景元素: 当不希望背景过于偏向薄荷绿或桃色时，提供一个更中立的柔和选择。
# - UI中的非激活或禁用状态的元素，但仍希望保持一定的可见性。
# - 阴影或远景的柔和色调。
# - 作为连接冷色调(TEAL_GREEN, PALE_MINT)和暖色调(LIGHT_PEACH, SOFT_PINK)的桥梁色之一。

# 10. #708090 (标准色) -> (112, 128, 144) - (一个经典的柔和蓝灰色，用于文本或深色点缀)
SLATE_GRAY_SOFT = (112, 128, 144) # 注意：这是一个标准颜色名，也可以自己调配更柔和的深色
# 英文名: Slate Gray (Soft variant) / Cool Dark Gray
# 配色建议:
# - 主要文本颜色: 在浅色背景上提供良好的可读性，比纯黑更柔和。
# - UI图标或边框的深色。
# - 需要与浅色背景形成对比的深色元素，但又不想用纯黑那么生硬。
# - 作为整个浅色调色板中的“锚点色”，增加视觉稳定性。

BLACK = (0,0,0)
WHITE = (255,255,255)

# --- 配色方案思路 (扩展后) ---
# 你现在有了更多的层次和选择：
# - 冷色系层次: TEAL_GREEN -> LIGHT_AQUA -> PALE_MINT -> VERY_PALE_MINT
# - 暖色系层次: SOFT_PINK -> PALE_ROSE -> LIGHT_PEACH -> PEACH_BLUSH
# - 中性/过渡色: DUSTY_CYAN_GRAY, SLATE_GRAY_SOFT (用于文本/强调)

# 例如，可以这样组合：
# - 背景: VERY_PALE_MINT 或 PEACH_BLUSH (选择一个主基调)
# - 主要UI: TEAL_GREEN
# - 次要UI/悬停: LIGHT_AQUA
# - 面板背景: PALE_MINT 或 LIGHT_PEACH
# - 强调/重要提示: SOFT_PINK
# - 次要提示/点缀: PALE_ROSE
# - 文本/深色图标: SLATE_GRAY_SOFT
# - 中性区域/分隔: DUSTY_CYAN_GRAY


# 背景颜色
BACKGROUND_COLOR = VERY_PALE_MINT

# 文本颜色
TEXT_COLOR = SLATE_GRAY_SOFT

# ------------------------------------------
# index
# 按钮悬停颜色
INDEX_TITLE_COLOR = SLATE_GRAY_SOFT
BUTTON_BEGIN_COLOR = TEAL_GREEN
BUTTON_BEGIN_HOVER_COLOR = LIGHT_AQUA

# ------------------------------------------





# ------------------------------------------
# Instruction 颜色
INSTRUCTION_COLOR = SLATE_GRAY_SOFT
INSTRUCTION_RETURN_COLOR = TEAL_GREEN
INSTRUCTION_RETURN_HOVER_COLOR = LIGHT_AQUA
INSTRUCTION_TITLE_COLOR = SLATE_GRAY_SOFT

# ------------------------------------------





# ------------------------------------------
# 玩家颜色
PLAYER_COLOR = PALE_ROSE
# ------------------------------------------





# ------------------------------------------
SCORE_COLOR = BLACK
# ------------------------------------------



# ------------------------------------------
GLASS_COLOR = (50, 150, 50)
EARTH_COLOR = (139, 119, 74)
ROAD_COLOR = (80, 80, 80)
# ------------------------------------------




# ------------------------------------------
ARTICLE_TEXT_COLOR = SLATE_GRAY_SOFT
ARTICLE_CHOOSE_BUTTON_COLOR = TEAL_GREEN
ARTICLE_CHOOSE_BUTTON_COLOR_HOVER = LIGHT_AQUA

ARTICLE_CHOOSEOVER_START__COLOR = TEAL_GREEN
ARTICLE_CHOOSEOVER_START__COLOR_HOVER  = LIGHT_AQUA

TEXT_COLOR_TYPED = WHITE
TEXT_COLOR_UNTYPED = BLACK
# ------------------------------------------





REBUGIN_BUTTON_COLOR = TEAL_GREEN
REBUGIN_BUTTON_COLOR_HOVER = LIGHT_AQUA
            
