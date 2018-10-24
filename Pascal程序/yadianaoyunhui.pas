var
  a,b,c,d,e:integer;
begin
  for a:=1 to 5 do
    for b:=1 to 5 do
      for c:=1 to 5 do
        for d:=1 to 5 do
        begin
          e:=15-a-b-c-d;
          if (ord(b=5)+ord(d=3)=1)and(ord(a=1)+ord(e=4)=1)and(ord(c=4)+ord(d=2)=1)and(ord(b=3)+ord(e=5)=1) and(a*b*c*d*e=120) then
          writeln('a:',a,' ','b:',b,' ','c:',c,' ','d:',d,' ','e:',e);
        end;
end.