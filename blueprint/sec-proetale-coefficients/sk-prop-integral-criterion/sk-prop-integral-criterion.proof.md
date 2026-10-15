+++
kind  = "proof"
of    = "sk-prop-integral-criterion"
uses = ["sk-thm-pe-constructible-comparison", "det-prop-integral-criterion-constant-coefficients"]
+++
For $\cO_E$ our definition of a constructible sheaf is Bhatt–Scholze, Definition 6.8.10,
and Bhatt–Scholze, Proposition 6.8.11(3) identifies bounded complexes with such cohomology
sheaves with the adic constructible derived category. The Stacks Project describes this
category by completeness and reduction (\stacks{09C0}, \stacks{09C1}), requiring the
reduction to have finite Tor dimension; here that condition is automatic, since
$\cO_E/\pi_E$ is a field. Two identifications connect that description with the statement.
First, the Stacks Project uses an auxiliary étale description of the reduction, and
[sk-thm-pe-constructible-comparison] identifies it with the pro-étale category. Second, it
works over the constant sheaf $\cO_E$, whereas our coefficient sheaf is $\cO_{E,X}$
([def-weil-completed-integral-coefficients]). The map between them is flat and an
isomorphism modulo every $\pi_E^n$, so restriction of scalars identifies the derived
complete objects on both sides together with their reductions (\stacks{099I});
see [det-prop-integral-criterion-constant-coefficients]. Under these identifications the two
criteria agree. The resulting description of $\Dbc(X,\cO_E)$ by completeness and
constructible reductions, with the uniform amplitude of the reductions made explicit, is
[def-weil-derived-complete-integral-detailed]; the equivalence of that description with the
criterion is [det-prop-integral-criterion-reductions].
