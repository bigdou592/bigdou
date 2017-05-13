3-1.把peoples表中school不是GDUFS的人全部找出来？（包括school为NULL的人）写出MySQL语句。
select name from peoples where school is not GDUFS and where school is NULL;
3-2.查找计算机系每次考试所有学生的平均成绩(最终显示学生姓名, 考试名称, 平均分)。
select name,exam_name,avg(grade) from peoples where dept_name is computer;
3-3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）。
select sex,name,grade from peoples where avg(grade)>=80;
3-4.找出人数最少的院系以及其年度预算。
select dept_name,gudget from peoples where dept_name=min(dept_name);
3-5.计算机系改名了，改成计算机科学系（comp. sci.），写出mysql语句。
UPDATE department SET dept_name=comp.sci WHERE dept_name=computer;
3-6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）。
UPDATE department SET budget=budget+count(dept_name)*2000;
3-7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.
INSERT INTO department (dept_name,building,budget) VALUES (avg_budget,NULL,avg(budget));
3-8. 删除计算机系中考试成绩平均分低于70的学生.
DELETE FROM department WHERE dept_name=computer and grade<avg(grade);
3-9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.
UPDATE student SET emotion_state=loving where emotion_state=single where avg(grade)<75;
