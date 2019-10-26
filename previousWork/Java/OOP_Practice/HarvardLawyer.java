//Jaewon Jeung. Thursday 3:00-4:00
package company;

public class HarvardLawyer extends Lawyer {
	public double getSalary() {
		return super.getSalary()*1.2;
	}
	
	public int getVacationDays() {
		return super.getVacationDays()+3;
	}
	

	public String getVacationForm() {
		return super.getVacationForm() + super.getVacationForm() + super.getVacationForm();
	}
}

//public int getVacationDays() {
//	return super.getVacationDays()+5;
//}

//public void sue() {
//	System.out.println("I'll see you in court!");
//}


