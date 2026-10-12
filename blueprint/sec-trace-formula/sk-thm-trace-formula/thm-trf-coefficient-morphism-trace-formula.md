+++
id = "thm-trf-coefficient-morphism-trace-formula"
kind = "theorem"
title = "Trace formula for Frobenius coefficient morphisms over a finite ring"
order = 2683
uses = ["d-lines", "d-relative-frob", "def-trf-admissibility", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-trf-frobenius-coefficient-morphism", "def-trf-weil-shriek-pushforward", "def-weil-finite-field-fiber", "def-weil-pbc-etale-origin-witness", "def-weil-scheme-morphism-properties", "fix-lem-finite-tor-perfect", "i-relative-frob", "i-topology", "lem-sf-proetale-constructible-origin", "lem-trf-chain-supertrace", "lem-trf-compactification-cohomology", "lem-trf-compactification-graph-operator", "lem-trf-global-operator-perfect", "lem-trf-weil-shriek-operator-fibres", "prop-trf-graph-operator", "prop-trf-trace-additivity-open-closed", "prop-trf-trace-formal-laws", "rem-ptr-trf-admissibility-12", "thm-sf-preservation-class", "thm-trf-frobenius-fixed-points", "thm-trf-frobenius-local-term", "thm-trf-lefschetz-verdier"]
+++
Fix the global finite-field datum $p,a,q,k_0,k$, where $q=p^a$, and
the coefficient conventions, $A=A_{E,n}$. Let $X_0$ be a separated
finite-type $k_0$-scheme, put $X=X_0\times_{k_0}k$, let
$K\in D^b_{ctf}(X,A)$ have an explicit etale-origin witness, and let
$\psi:L\Phi^*K\to K$ be a Frobenius coefficient morphism of
[def-trf-frobenius-coefficient-morphism], with iterates $\psi_m$ and
global operators $F_{c,m}(\psi)$; no invertibility of $\psi$ is
assumed. Assume the exceptional-adjoint admissibility hypotheses of
[def-trf-admissibility] for the graph correspondences and fixed-point
base changes on a chosen compactification defined over $k_0$, as in
the Grothendieck–Lefschetz formula over a finite ring below (at the
finite stage these hold automatically, and the proof does not use
them). For
$y\in X_0(\mathbf F_{q^m})$ with geometric point $\bar y$ one has
$\Phi^m\bar y=\bar y$ (the fixed points of
[thm-trf-frobenius-fixed-points]), and $\psi_m$ induces a stalk
endomorphism
$\psi_{m,\bar y}:K_{\bar y}\cong(L\Phi^{m*}K)_{\bar y}\to K_{\bar y}$.
Then for every $m\geq1$

$$
\boxed{
\operatorname{tr}_A\bigl(F_{c,m}(\psi)\mid R\Gamma_c(X,K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_A\bigl(\psi_{m,\bar y}\mid K_{\bar y}\bigr)
}
$$

in $A$, both sides being categorical traces of endomorphisms of
perfect complexes. This is the coefficient-morphism variant of the
finite-coefficient trace formula; for the scheme-Frobenius map
$\psi=u_1$ of a strict Weil complex it gives the
Grothendieck–Lefschetz formula over a finite ring.
