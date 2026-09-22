+++
id = "lem-kun-minimal-cohomology"
kind = "lemma"
title = "First cohomology of a bounded-below complex"
order = 6061
lean = ["AlgebraicGeometry.Etale.cohomology_eq_h0_of_minimal_degree"]
uses = ["def-weil-pbc-hypercohomology-filtrations", "def-kun-rgamma-unbounded"]
+++
Let $X$ be a scheme and $E\in\Dplus(X_{\Et})$. If $i$ is minimal with
$\mathcal H^i(E)\ne0$, then $H^i(X_{\Et},E)=H^0(X_{\Et},\mathcal H^i(E))$.

## Proof

By the hypercohomology spectral sequence for the structure (or identity)
morphism — in the form
$E_2^{p,q}=H^p(X_{\Et},\mathcal H^q(E))\Rightarrow H^{p+q}(X_{\Et},E)$ —
only the terms with $\mathcal H^q(E)\ne0$ contribute. By minimality of $i$,
$q=i$ is the only possible degree with $p+q=i$, so
$H^i(X_{\Et},E)=E_\infty^{0,i}=E_2^{0,i}=H^0(X_{\Et},\mathcal H^i(E))$.

Unresolved dependencies: def:weil-pbc-derived-categories
