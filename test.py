q1 = pn.widgets.TextInput(name="Input your first question", placeholder="Task", sizing_mode="stretch_width")
q2 = pn.widgets.TextInput(name="Input your second question", placeholder="Task", sizing_mode="stretch_width")

out1= pn.pane.Markdown("Answer1")
out2 = pn.pane.Markdown("Answer2")

answr_btn = pn.widgets.Button(name="Answer", button_type="primary", width=50, height=50)
answr_btn.on_click(btn_click)

def default(question:str):
    answer="Your question is: "+question
    print("input_function",answer)
    return answer 


def btn_click(event):
    if answer_button.clicks > 0:
        bound_q1 = pn.bind(default, q1)
        bound_q2 = pn.bind(default, q2)
        answer1 = bound_q1()
        answer2 = bound_q2()
    else:
        answer = "Error 404"
    
    output.object = answer
        
        
Tab = pn.Column(
            pn.Row(q1),
            pn.Row(q2),
            pn.panel(answer_button, loading_indicator=True, height=50),
            pn.layout.Divider(),
            pn.panel(output, loading_indicator=True, height=900),
            sizing_mode="stretch_width"
        )


layout = pn.Column(pn.Tabs(('Answer', Tab)))
layout.show()
