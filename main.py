import random
import matplotlib.pyplot as plt
from benchmarkFunctions import SphereFunction
from benchmarkFunctions import BentCigarFunction
from benchmarkFunctions import RastriginsFunction
from benchmarkFunctions import AckleysFunction
from geneticAlgorithmSolver import GeneticAlgorithmSolver
def main():
    vc = 40
    functionList = [SphereFunction,
                    BentCigarFunction,
                    RastriginsFunction,
                    AckleysFunction]
    functionNameList = ['SphereFunction',
                        'BentCigarFunction',
                        'RastriginsFunction',
                        'AckleysFunction']

    pc = 50
    for function in functionList:
        populationErrorList = []
        #------------- Classic algorithm
        random.seed(1)
        solver = GeneticAlgorithmSolver(function = function,
                                        vc = vc,
                                        pc = pc)
        solver.solve()
        populationErrorList.append(solver.getPopulationErrorList())
        #------------- (compare after cross over)
        random.seed(1)
        solver = GeneticAlgorithmSolver(function = function, vc = vc,  pc = pc, comAftCro = True )
        solver.solve()
        populationErrorList.append(solver.getPopulationErrorList())
       #-------------(compare candidate populations)
        random.seed(1)
        solver = GeneticAlgorithmSolver(function = function,
                                        vc = vc,
                                        pc = pc,
                                        compCandPop = True
                                        )
        solver.solve()
        populationErrorList.append(solver.getPopulationErrorList())
        #------------- (compare after mutation)
        random.seed(1)
        solver = GeneticAlgorithmSolver(function = function,
                                        vc = vc,
                                        pc=pc,
                                        compAftMu = True
                                        )
        solver.solve()
        populationErrorList.append(solver.getPopulationErrorList())
        #-------------(all together)
        random.seed(1)
        solver = GeneticAlgorithmSolver(function = function, vc = vc,  pc = pc, comAftCro = True,
                                        compCandPop = True,
                                        compAftMu = True
                                        )
        solver.solve()
        populationErrorList.append(solver.getPopulationErrorList())
        #------------- Plot populationErrorList
        xpoints = range(0, pc)
        ypoints0 = populationErrorList[0]
        ypoints1 = populationErrorList[1]
        ypoints2 = populationErrorList[2]
        ypoints3 = populationErrorList[3]
        ypoints4 = populationErrorList[4]
        lineWidth = 2
        plt.rcParams['figure.figsize'] = (15,5)
        plt.plot(xpoints, ypoints0, color='black',
                 linewidth=lineWidth,
                 label='Classic algorithm')
        plt.plot(xpoints, ypoints1, color='red',
                 linewidth=lineWidth,
                 label='select new father')
        plt.plot(xpoints, ypoints2, color='orange',
                 linewidth=lineWidth,
                 label='select new generation')
        plt.plot(xpoints, ypoints3, color='green',
                 linewidth=lineWidth,
                 label='new model of crossover')
        plt.plot(xpoints, ypoints4, color='blue',
                 linewidth=lineWidth,
                 label='combination')
        plt.xlabel('Population')
        plt.ylabel('Error')
        plt.title(functionNameList[functionList.index(function)])
        plt.legend()
        plt.show()
    #---------------------------------------------------------------------
    # Compare mean error of classic and 4 enhanced algorithms
    # on 4 benchmark functions
    #---------------------------------------------------------------------
    iterationCount = 51
    pc = 300
    for function in functionList:
        #------------- Classic algorithm
        sumError = 0.0
        meanError = 0.0
        random.seed(1)
        for i in range(0, iterationCount):
            solver = GeneticAlgorithmSolver(function = function,
                                            vc = vc,
                                            pc = pc
                                            )
            sumError += solver.solve()
        meanError = float(sumError / iterationCount)
        print("-----------------------------------------")
        print("Classic algorithm for "
              + functionNameList[functionList.index(function)] + ":")
        print(meanError)
        #------------- 1 (compare after cross over)
        sumError = 0.0
        meanError = 0.0
        random.seed(1)
        for i in range(0, iterationCount):
            solver = GeneticAlgorithmSolver(function = function, vc = vc,  pc = pc, comAftCro = True,)
            sumError += solver.solve()
        meanError = float(sumError / iterationCount)
        print("select father (compare after cross over):")
        print(meanError)
        #------------- 2 (compare candidate populations)
        sumError = 0.0
        meanError = 0.0
        random.seed(1)
        for i in range(0, iterationCount):
            solver = GeneticAlgorithmSolver(function = function,
                                            vc = vc,
                                            pc = pc,
                                            compCandPop = True
                                            )
            sumError += solver.solve()
        meanError = float(sumError / iterationCount)
        print("select new generation (compare candidate populations):")
        print(meanError)
        #-------------  3 (compare after mutation)
        sumError = 0.0
        meanError = 0.0
        random.seed(1)
        for i in range(0, iterationCount):
            solver = GeneticAlgorithmSolver(function = function,
                                            vc = vc,
                                            pc = pc,
                                            compAftMu = True
                                            )
            sumError += solver.solve()
        meanError = float(sumError / iterationCount)
        print("new model of mutation (compare after mutation):")
        print(meanError)
        #------------- 4 (all together)
        sumError = 0.0
        meanError = 0.0
        random.seed(1)
        for i in range(0, iterationCount):
            solver = GeneticAlgorithmSolver(function = function, vc = vc,  pc = pc, comAftCro = True,
                                            compCandPop = True,
                                            compAftMu = True
                                            )
            sumError += solver.solve()
        meanError = float(sumError / iterationCount)
        print("combination (all together)")
        print(meanError)
    #---------------------------------------------------------------------
if __name__ == "__main__":
    main()
