//Jaewon Jeung. Thursday 3:00-4:00
package company;

public class EmployeeClient {
	public static void main(String[]args) {
		Lawyer law = new Lawyer();
		SoftwareEngineer eng = new SoftwareEngineer();
		HarvardLawyer hl = new HarvardLawyer();
		printEmployee(law);
		System.out.println();
		printEmployee(eng);
		System.out.println();
		printEmployee(hl);
	}
	
	public static void printEmployee(Employee emp) {

		if (emp instanceof SoftwareEngineer) {
			SoftwareEngineer sf = (SoftwareEngineer) emp;
			System.out.println("Software Engineer:");
			sf.writeCode();
		}
		else if (emp instanceof HarvardLawyer) {
			HarvardLawyer newhl = (HarvardLawyer) emp;
			System.out.println("Harvard Lawyer:");
			newhl.sue();
		}
		else if (emp instanceof Lawyer) {
			Lawyer newl = (Lawyer) emp;
			System.out.println("Lawyer:");
			newl.sue();
		}
		System.out.println("Salary: " + emp.getSalary());
		System.out.println("Hours: " + emp.getHours());
		System.out.println("Vacation days: " + emp.getVacationDays());
		System.out.println("Vacation form: " + emp.getVacationForm());		
	}
}
