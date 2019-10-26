//Jaewon Jeung. Thursday 3:00-4:00
package company;

public class Lawyer extends Employee {
	public int getVacationDays() {
		return super.getVacationDays()+5;
	}
	public String getVacationForm() {
		return "pink";
	}
	public void sue() {
		System.out.println("I'll see you in court!");
	}
}
