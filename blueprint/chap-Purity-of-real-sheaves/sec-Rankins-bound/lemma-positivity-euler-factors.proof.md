+++
kind = "proof"
of = "lemma-positivity-euler-factors"
order = 1159
uses = ["lemma-filtrations-spectra"]
+++
We write an inverse characteristic polynomial as the exponential of a
series in the traces of powers, whose coefficients are then visibly
nonnegative. For a square matrix $A$, triangularizing $A$ and expanding
the logarithm of each factor we get the formal identity

$$
\det(1-tA)^{-1}
=\exp\left(\sum_{n\ge1}\operatorname{Tr}(A^n)\frac{t^n}{n}\right).
$$

On an even tensor power, the trace of the $n$th power of Frobenius is
$\operatorname{Tr}(\operatorname{Frob}_x^n\mid\mathcal G)^{2m}$. Since
$\mathcal G$ is real, this is nonnegative after applying $\iota$.  Every
coefficient of the exponential is then a finite sum of products of nonnegative
numbers. This remains true after replacing $t$ by $t^{\deg(x)}$.
