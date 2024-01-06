x = MsgBox("Nithra we have hardly 540 days in this college life, So I want to straight to the point...")
x = MsgBox("I just wanted to say that I'm absolutely crazy about you! 🌟 I love how you bring excitement and joy into my life. You know, I enjoy doing crazy things, and I've found my perfect partner in crime...that's you! 🤪")
x = MsgBox("And hey, about those studies, I've got to admit, you're pretty amazing. But here's the thing, I like a good challenge! 😏 I'm up for it! Let's embark on this crazy journey together, study hard, and create some unforgettable moments. What do you say? 😄")

Do
    response = MsgBox("I love you, do you love me?", vbYesNo + vbQuestion, "Love Check")
    If response = vbYes Then
        MsgBox "Great! Love you too!", vbInformation, "Love Confirmed"
        Exit Do
    End If
Loop