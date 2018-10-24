var
  xt:char;
begin
  for xt:='a'to'b'do
    if ord(xt<>'a')+ord(xt='c')+ord(xt<>'d')+ord(xt='d')=3 then
    begin
      writeln(xt);
      exit;
    end;
end.
