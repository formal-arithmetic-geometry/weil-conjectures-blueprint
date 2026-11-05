+++
id = "prose-00-01"
kind = "hidden"
title = "Abstract"
order = 1
+++
Let $X$ be a smooth projective variety of dimension $d$ over $\mathbf F_q$.
The Weil conjectures assert that its zeta function, which counts the points
of $X$ over all the fields $\mathbf F_{q^m}$, is a rational function, that it
satisfies a functional equation, and that its zeros lie on the circles
$|T|=q^{-i/2}$ with $i$ odd and its poles on those with $i$ even, an analogue
of the Riemann hypothesis. The points over $\mathbf F_{q^m}$ are the fixed
points of the $m$th power of Frobenius. Weil therefore expected the first two
statements to follow from a Lefschetz fixed point formula and Poincaré
duality in a cohomology theory with coefficients of characteristic zero.
These notes construct such a theory and prove all three statements.

The theory is $\ell$-adic cohomology. Étale cohomology works best with the
torsion coefficients $\mathbf Z/\ell^n$, but traces must be taken in
characteristic zero. On the pro-étale site of Bhatt and Scholze,
$\mathbf Z_\ell$ and $\mathbf Q_\ell$ define sheaves of rings just as
$\mathbf Z/\ell^n$ does, so one set of definitions and one formalism of six
operations serve every coefficient ring. The trace formula and Poincaré
duality then give rationality and the functional equation.

The Riemann hypothesis follows from the Deligne–Laumon theorem, which bounds
the absolute values of Frobenius eigenvalues, the weights, on the cohomology
of sheaves. We follow Laumon's proof: fibring by curves reduces the theorem to
curves, where the $\ell$-adic Fourier transform and a positivity argument that
Deligne took from Rankin bound the weights.

The documents speak some of the most important definitions and theorems in our lean formalization. They quote some
foundational results from algebraic geometry and from étale cohomology with
torsion coefficients, each stated precisely. We assume a first course in
algebraic geometry and some familiarity with derived categories and singular
cohomology, but no étale cohomology.
