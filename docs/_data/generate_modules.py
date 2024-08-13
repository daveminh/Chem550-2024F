table = """M	8/19	No class - Dr. Minh conference travel	
W	8/21	No class - Dr. Minh conference travel	
M	8/26	Introduction and syllabus. Operators.	
W	8/28	Bra-ket notation. Postulates.	
M	9/2	No class - Labor Day	
W	9/4	The Heisenberg uncertainty principle. Wave functions.	
M	9/9	Exercise 1: Google Colab. One-dimensional model systems: Free particle. Particle in a box. Tunneling. Harmonic oscillator + vibrational spectroscopy. 	HW 1
W	9/11	Rotation: Particle on a ring. Angular momentum. Rigid rotor + rotational spectroscopy.	
M	9/16	Spherical systems: Particle on a sphere. Spherical harmonics. Hydrogenic atoms. 	Exercise 1. HW 2
W	9/18	Ladder operators. Spin.	
M	9/23	Midterm 1: Analytical Systems.	HW 3
W	9/25	Variation theory. Raleigh-Ritz.	
M	9/30	Perturbation theory.	
W	10/2	Many-electron atoms. Slater determinants.	
M	10/7	No class - Fall Break Day	
W	10/9	Born-Oppenheimer approximation and H+.	HW 4
M	10/14	Molecular orbital theory.	
W	10/16	Hartree-Fock Method. Basis sets.	
M	10/21	Midterm 2: Approximation Methods.	
W	10/23	Exercise 2: Introduction to molecular modeling	
M	10/28	Exercise 3: Choice of basis set	
W	10/30	Post Hartree-Fock Methods. Configuration Interaction.	Exercise 2
M	11/4	Exercise 4: Single-point energies	Exercise 3
W	11/6	Exercise 5: Electron densities and electrostatic potentials	
M	11/11	Exercise 6: Computing spectroscopic and thermochemical properties	Exercise 4. Select molecules.
W	11/13	Exercise 7: Transition states	Exercise 5
M	11/18	Project Proposals. After class if needed.	Exercise 6
W	11/20	Midterm 3: Molecular Modeling.	Exercise 7
M	11/25	During lunch: Interpretations of Quantum Mechanics. Exercise 8: Quantum Mechanics/Molecular Mechanics (QM/MM) calculations.	
W	11/27	No class - Thanksgiving Break	"""

for row in table.split('\n'):
    cols = row.split('\t')
    day = cols[0]
    date = cols[1]
    record = f"- day: {day}\n  date: {date}\n"
    if len(cols)>2:
        content = cols[2].strip('.')
        basename = content.split('.')[0]
        if content.find("Exercise")>-1:
            exercise_info = content[content.find('Exercise'):].split('.')[0]
            title = content.replace(exercise_info,'')
            if title!="":
                record += f'  title: "{title}"\n'
            record += f'  exercise: "{exercise_info[9:]}"\n'
            if content.find('.')>0:
                basename = content[content.find('.'):]
            else:
                basename = ''
        else:
            title = content
            record += f'  title: "{title}"\n'
        if basename.find('No class')>-1:
            basename = ''
        if basename!="":
            dash_date = '-'.join([f"{int(d):02d}" for d in date.split('/')])
            record += f'  basename_template: "{dash_date}-{basename}"\n'
    if len(cols)>3:
        due = cols[3].strip('.')
        if due!="":
            record += f'  due: "{due}"\n'
    # record += '\n'
    print(record)