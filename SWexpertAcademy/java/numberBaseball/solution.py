class UserSolution {
    public final static int N = 4;
    public void doUserImplementation(int guess[]) {
        Solution solution = new Solution();
        Solution.Result result = new Solution.Result();        
        int s;
        int b;
        int sb;
        int c1[] = {0,1,2,3};
        int c2[] = {4,5,6,7};

        result = solution.query(c1);
		s = result.strike;
        b = result.ball;
        result = solution.query(c2);
        s = s + result.strike;
        b = b + result.ball;
        sb = s+b;
        
        if(sb == 2){ // 8,9 모두 포함
            //남은건 0,1,2,3,4,5,6,7
			c1 = {0,1,2,3};
            result = solution.query(c1);
            sb = result.strike + result.ball;
            if(sb == 0){ // 
                
            }else if(sb == 1){
                
            }else if(sb == 2){
                
            }
            
        }else if(sb == 3){ // 8,9 중 하나 포함

        }else{ // 8,9 모두 제와

        }
        
        // Implement a user's implementation function
        //
        // The array of guess[] is a return array that
        // is your guess for what digits[] would be.
    }
}
