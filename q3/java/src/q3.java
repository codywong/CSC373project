import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;


public class q3 {
	public static void main(String args[]) {
		String fileName = args[0];
		int m = 0;
		int n=0;
		String[][] S=null;
		String[][] T=null;
		int[] result=null;
		
		try {
			
			// Read m, n, S, T from file
			BufferedReader br = new BufferedReader(new FileReader(fileName));
			String line;
			int lineNo=0;
			while(br.ready()) {
				line=br.readLine();
				if(isComment(line))
					continue;
				else
				{	
					lineNo++;
					if(lineNo==1)
					{
						m=Integer.parseInt(line);
						//System.out.println("m is "+m+" n is "+n);
					}
					else if(lineNo==2)
					{
						n=Integer.parseInt(line);
						S = new String[m][n];
						T = new String[m][n];
						result = new int[n];
					}
					else
					{
						if(lineNo<m+3)
						{
							append(line, S, lineNo-3,n);
						}
						else if(lineNo < 2*m+3)
						{
							append(line, T, lineNo-m-3,n);
						}
						else
							throw new Exception("More than 2m lines are read.");
					}
					//System.out.println(line);
				}
			}
			
			//process every column of shipping
			for(int k=0;k<n;k++)
			{
				int sLast=findLast(S,k,m);
				int tLast=findLast(T,k,m);
				int [][] d = new int[sLast+1][sLast+1];
/*				String [] A= new String[sLast];
				String [] B = new String [sLast];
				for()
*/				//initialize D[i][0]=i, for i<=m 
				//D[1][1]= 1, if S[1] != T1 ; D[1][1]= 0, if C1 = C1
				for(int i=0;i<sLast+1;i++)
				{
					d[i][0]=i;
				}
				if(!S[m-1][k].equals(T[m-1][k]))
					d[1][1]=1;
				else
					d[1][1]=0;
				
				//build from bottom up
				//for 1<=i<=m, j<=i and j<=n
				//calculate remove, swap and same
				//D[i][j] = min {remove, swap, same}
				int i;
				int j;

				for(i=1;i<sLast+1;i++)
				{
					for(j=1;j<i+1 && j<tLast+1;j++)
					{
						int remove=-1,swap=-1,same=-1;
						int min=m;
						if(i==1 && j==1)
							continue;
						if(j<i)
							remove = d[i-1][j]+1;
						if(S[m-i][k].equals(T[m-j][k]))
							same= d[i-1][j-1];
						else
							swap= d[i-1][j-1]+1;
						if(remove!=-1)
							min=remove;
						if(swap!=-1 && swap<min)
							min=swap;
						if(same!=-1 && same < min)
							min=same;
						d[i][j]=min;
					}
				}

				//for 0<=j<=n, calculate D[m][j]+(n-j),  D[m][n]= min{D[m][j]+(n-j)}
				int minMN=m;
				for(j=0;j<=tLast && j<=sLast;j++)
				{
					int temp = d[sLast][j]+(tLast-j);
					if(temp < minMN)
						minMN= temp;
				}
				/*for(int c=0;c<sLast+1;c++)
				{
					for(int f=0;f<sLast+1;f++)
					{
						System.out.print(d[c][f]+" ");
					}
					System.out.println();
				}*/
				
				result[k]=minMN;
				//System.out.println(result[k]);
			}
			int r=0;
			for(int i: result)
			{
				r+=i;
			}
			/*System.out.println("m is "+m+" n is "+n);
			System.out.println("S is "+S);*/
			System.out.println(r);
		} catch (FileNotFoundException e) {
			System.out.println("Cannot open the file.");
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println("Cannot read lines.");
			e.printStackTrace();
		} catch (Exception e) {
			System.out.println(e.getMessage());
			e.printStackTrace();
		}
		     
	}

	//number of of A or B 
	private static int findLast(String[][] s, int k, int m) {
		for(int i=0;i<m;i++)
		{
			if(!s[i][k].equals("-"))
				return m-i;
		}
		return 0;
	}

	private static void append(String line, String[][] s, int lineNo, int n) throws Exception {
			String[] strings = line.split(" ");
			if(strings.length!=n)
				throw new Exception("Number of characters in a line is not equal to n.");
			for(int i=0;i<strings.length;i++)
				s[lineNo][i]=strings[i];
	}

	private static boolean isComment(String line) {
		Pattern p= Pattern.compile("#.*");
		Matcher m=p.matcher(line);
		
		return m.find();
	}
}
