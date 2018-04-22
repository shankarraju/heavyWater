  $(document).ready(function(){
        
       var x= $(document).width();
        var y=Math.round(x/50);
        console.log("y",y);
        for(var i=0;i<y;i++){
            $("#bar").append('<div class="inner-class"><span class="object"></span><span class="object"></span><span class="object"> </span> <span class="object"> </span></div>')
        } 
        
        $(window).on('resize',function(){
            $("#bar").html("");
            var x= $(document).width();
        var y=Math.round(x/50);
        console.log("y",y);
        for(var i=0;i<y;i++){
            $("#bar").append('<div class="inner-class"><span class="object"></span><span class="object"></span><span class="object"> </span> <span class="object"> </span></div>')
        }
            
        })
        
        $.get('/getSession',function(data){
            if(data.output=='success' && (data.session_user=='shankar' || data.session_user=='heavywater')){
                $("#first").hide();
                $("#authBox").hide();
                 $("#dashBoard").slideDown();
            }
        })
        $(document).on('click','#backButton',function(){
             $("#resultBox").hide();
            $("#dashBoard").slideDown();
        })
        $(document).on('click',"#start",function(){
            console.log("clicked!");
            $("#first").hide();
            $("#authBox").slideDown();
        
        })
        
        $("#authForm").submit(function(e){
            e.preventDefault();
            $("#load").show();
            $.post($(this).attr('action'),$(this).serialize(),function(data){
                console.log(JSON.stringify(data));
                if(data==true){
                    $("#authBox").hide();
                    $("#load").hide();
                    $("#dashBoard").slideDown();
                    
                }
                else{
                    $("#load").hide();
                    $("#authBox").effect("shake"); 
                }
            },dataType='json')
            
        })
        
        $("#searchBox").submit(function(e){
            e.preventDefault();
            $("#load").show();
            var userSel=$('#searchBox input[type=radio][name=selectOption]:checked').val();
            var inp_str=$('#searchBox textarea[name=inp_str]').val();
            console.log(userSel)
            if(userSel=="post"){
                console.log("INSIDE POST")
                $.post('/test',{inp_str:inp_str},function(data){
                    console.log(data);
                    console.log(data.out);
                    $("#dashBoard").hide();
                    $("#res").html(data.out);
                    $("#resultBox").slideDown();
                    $("#load").hide();
                },dataType='json').fail(function(){
                    $("#load").hide();
                })
                
            }
            
            if(userSel=="get"){
                console.log("INSIDE GET")
                $.get('/testGet/ '+inp_str+'',function(data){
                    console.log(data)
                    $("#load").hide();
                    $("#dashBoard").hide();
                     $("#res").html(data.out);
                    $("#resultBox").slideDown();
                },dataType='json').fail(function(){
                    $("#load").hide();
                })
            }
            
        })
    })