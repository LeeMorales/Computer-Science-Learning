var
  i,x,a:longint;
begin
  repeat
    a:=i mod 100 div 10;
    i:=i+1;
   begin
     until(i div 100 mod 10=1) and (i mod 81=0) and (i mod 91=0) and (a=1);
   write(i);
   end;
end.