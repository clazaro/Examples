# Elliptic benchmark problem

**Author:** [Riccardo Tosi](https://riccardotosi.github.io)

**Kratos version:** 8.1

**XMC version:** Kratos default version

**PyCOMPSs version:** Kratos default version to run in serial, >2.8 to run with `runcompss`

**Source files:** [Synchronous Monte Carlo](synchronous_monte_carlo), [Asynchronous Monte Carlo](asynchronous_monte_carlo), [Synchronous Multilevel Monte Carlo](synchronous_multilevel_monte_carlo), [Asynchronous Multilevel Monte Carlo](asynchronous_multilevel_monte_carlo)

**Application dependencies:** `ConvectionDiffusionApplication`, `LinearSolversApplications`, `MeshingApplication`, `MultilevelMonteCarloApplication`

## Case Specification
Let's consider the stationary heat equation with a varying heat flux, a square two-dimensional domain and Dirichlet boundary conditions. The problem reads as:

* <img src="https://render.githubusercontent.com/render/math?math=\nabla \cdot k \nabla \phi = \varepsilon f \ , \quad \phi \in \Omega">
* <img src="https://render.githubusercontent.com/render/math?math=\phi = 0 \ , \quad \phi \in \partial \Omega">

where <img src="https://render.githubusercontent.com/render/math?math=\Omega=[0,1]\times[0,1]">, <img src="https://render.githubusercontent.com/render/math?math=f=-432(x^2+y^2-x-y)"> and <img src="https://render.githubusercontent.com/render/math?math=\varepsilon \sim \beta(2,6)">, i.e. <img src="https://render.githubusercontent.com/render/math?math=\varepsilon"> follows a beta distribution. The thermal diffusivity is <img src="https://render.githubusercontent.com/render/math?math=k=1"> for simplicity. The Quantity of Interest (QoI) we are interested in is the integral over the whole domain of the temperature, meaning:

<img src="https://render.githubusercontent.com/render/math?math=QoI=\int_{\Omega}\phi(x,y)dxdy \,.">

The problem can be run with four different algorithms and we refer to [1] for details:

* Synchronous Monte Carlo (SMC),
* Asynchronous Monte Carlo (AMC),
* Synchronous Multilevel Monte Carlo (SMLMC),
* Asynchronous Multilevel Monte Carlo (AMLMC).

Apart from the scheduling, which may be synchronous or asynchronous, similar settings are employed. We refer, for example, to: number of samples estimation, number of indices estimation, maximum number of iterations, tolerance, confidence, etc. Such settings can be observed in the corresponding configuration file of each algorithm, located inside the `problem_settings` folder.

To run the examples, the user should go inside the folder-algorithm of interest and run the `run_mc/mlmc_Kratos.py` Python file. In case one wants to use PyCOMPSs, the user should execute `./run_with_pycompss.sh` from inside the folder of interest.

## Results

The expected result is to observe statistical accuracy and scheduling parallelism for the asynchronous algorithms.

<img src="results/poisson.png" alt="temperature" width="700"/>

Concerning statistical accuracy, the QoI we obtain is consistent with literature results [2]. This ensures the correct implementation of XMC and its integration with Kratos Multiphysics.

We report the graph dependencies of SMC and of AMC to compare synchronous and asynchronous algorithms. The figure below shows the increased parallelism provided by the asynchronous algorithm, with respect to the synchronous one.

SMC:

<img src="results/SMC_graph.PNG" alt="SMC" width="700"/>

AMC:

<img src="results/AMC_graph.PNG" alt="AMC" width="700"/>

SMLMC and AMLMC graphs present similar behaviors, with the difference that samples are run on different accuracy levels.

## References

[1] Tosi, R., Amela, R., Badia, R., & Rossi, R. (2021). A parallel dynamic asynchronous framework for Uncertainty Quantification by hierarchical Monte Carlo algorithms. Journal of Scientific Computing, 89(28), 25. https://doi.org/10.1007/s10915-021-01598-6

[2] Pisaroni, M., Krumscheid, S., & Nobile, F. (2020). Quantifying uncertain system outputs via the multilevel Monte Carlo method — Part I: Central moment estimation. Journal of Computational Physics. https://doi.org/10.1016/j.jcp.2020.109466
