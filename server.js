//REST API demo in Node.js
var express = require('express'); // requre the express framework
var app = express();
var path = require('path');
var fs = require('fs'); //require file system object
const { json } = require('express');

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, 'id.json'));
});
app.post('/', function(req, res) {
    var mongojs=require("mongojs");
	var cs="mongodb+srv://mahesh:mahesh@cluster0.qe4fh.mongodb.net/Tie?retryWrites=true&w=majority"
	var db=mongojs(cs,["id"])
	var d={
		id:parseInt(req.query.id),
		password:req.query.signuppswd
	}
	
    db.id.find(d,function(err,docs){
		if(docs.length==0){
			res.send("please check your username and password");
		}
		else{
			res.send("OK");
		}
	})
});

app.get("/leavebalance",function(req,res){
	res.sendFile(path.join(__dirname, 'leavebalance.json'));
})
app.post("/leavebalance",function(req,res){
	var mongojs=require("mongojs");
	var cs="mongodb+srv://mahesh:mahesh@cluster0.qe4fh.mongodb.net/Tie?retryWrites=true&w=majority"
	var db=mongojs(cs,["leavebalance"])
	var d={
		id:parseInt(req.query.id)
	}
    db.leavebalance.find(d,function(err,docs){
		if(docs.length==0){
			res.send("please check your id and password");
		}
		else{
			res.send(docs[0].leavebalance+'');
		}	
	})	
})

app.get("/salaryissue",function(req,res){
	res.sendFile(path.join(__dirname, 'salaryissue.json'));
})
app.post("/salaryissue",function(req,res){
	var mongojs=require("mongojs");
	var cs="mongodb+srv://mahesh:mahesh@cluster0.qe4fh.mongodb.net/Tie?retryWrites=true&w=majority"
	var db=mongojs(cs,["salaryissue"])
	var d={
		id:parseInt(req.query.id),
		msg:req.query.salaryissue
	}
    db.salaryissue.insert(d,function(err,docs){
		if(docs.length==0){
			res.send("please check your id and password");
		}
		else{
			res.send("We have received your salaryissue we will soon resolve it");
		}	
	})	
})

app.get("/harassment",function(req,res){
	res.sendFile(path.join(__dirname, 'harassment.json'));
})
app.post("/harassment",function(req,res){
	var mongojs=require("mongojs");
	var cs="mongodb+srv://mahesh:mahesh@cluster0.qe4fh.mongodb.net/Tie?retryWrites=true&w=majority"
	var db=mongojs(cs,["harassment"])
	var d={
		id1:parseInt(req.query.id1),
		case:req.query.case,
		id2:req.query.id2
	}
    db.harassment.insert(d,function(err,docs){
		if(docs.length==0){
			res.send("please check your id and password");
		}
		else{
			res.send("Harassment case has been filed against "+req.query.id2+" a quick action will be taken");
		}	
	})	
})

app.get("/resignation",function(req,res){
	res.sendFile(path.join(__dirname, 'resignation.json'));
})
app.post("/resignation",function(req,res){
	var mongojs=require("mongojs");
	var cs="mongodb+srv://mahesh:mahesh@cluster0.qe4fh.mongodb.net/Tie?retryWrites=true&w=majority"
	var db=mongojs(cs,["resignation"])
	var d={
		id:parseInt(req.query.id),
		msg:req.query.resignissue,
		purpose:req.query.block
	}
    db.resignation.insert(d,function(err,docs){
		if(docs.length==0){
			res.send("please check your id and password");
		}
		else{
			res.send("We have received your resign request,HR will contact you soon");
		}	
	})	
})

/*app.get("/payslip",function(req,res){
	res.sendFile(path.join(__dirname, 'resignation.json'));
})*/
app.post("/payslip",function(req,res){
	var mongojs=require("mongojs");
	var cs="mongodb+srv://mahesh:mahesh@cluster0.qe4fh.mongodb.net/Tie?retryWrites=true&w=majority"
	var db=mongojs(cs,["payslip"])
	var d={
		id:parseInt(req.query.id),
	}
    db.payslip.find(d,function(err,docs){
		if(docs.length==0){
			res.send("please check your id and password");
		}
		else{
			res.send("Basic Salary: "+docs[0].basicsalary+''+"\n"+"Bonus: "+docs[0].bonus+''+"\n"+"HRA: "+docs[0].hra+''+"\n"+"DA: "+docs[0].da+'');
		}	
	})	
})

app.post("/reimbursment",function(req,res){
	var mongojs=require("mongojs");
	var cs="mongodb+srv://mahesh:mahesh@cluster0.qe4fh.mongodb.net/Tie?retryWrites=true&w=majority"
	var db=mongojs(cs,["reimbursment"])
	var on = {
		project:req.query.project,
		date_travel:req.query.date_travel,
		total_expenses:req.query.total_expenses
	}
	var bc = {
		project:req.query.project,
		total_expenses:req.query.total_expenses
	}
	var transfer = {
		transfer_date:req.query.transfer_date,
		total_expenses:req.query.total_expenses
	}
	var othe = {
		purpose:req.query.purpose,
		project:req.query.project,
		total_expenses:req.query.total_expenses
	}
	var d={
		id:parseInt(req.query.id),
		onsite:on,
		bcp:bc,
		transfertravel:transfer,
		other:othe
	}
	var d1={};
	d1["id"] = d["id"];
	if(!(d['onsite']===undefined)){
		d1["onsite"] = d["onsite"];
	}
	if(!(d['bcp']===undefined)){
		d1["bcp"] = d["bcp"];
	}
	if(!(d['transfertravel']===undefined)){
		d1["transfertravel"] = d["transfertravel"];
	}
	if(!(d['other']===undefined)){
		d1["other"] = d["other"];
	}
    db.reimbursment.insert(d1,function(err,docs){
		if(docs.length==0){
			res.send("please check your id and password");
		}
		else{
			res.send("ok");
		}	
	})	
})

app.listen(process.env.PORT || 4000, function(){
    console.log('Your node js server is running');
});