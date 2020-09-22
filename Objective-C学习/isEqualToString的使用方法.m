NSString *thing1 = @"Hello 5";
NSString *thing2 = [NSString strigWithFormat: @"Hello %d", 5];

if ([thing1 isEqualToString : thing2]){
    NSLog(@"They are the same");
}
