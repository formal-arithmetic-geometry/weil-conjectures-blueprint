+++
kind  = "proof"
of    = "prop-pod-integral-degreewise-form"
uses = ["sk-lem-finite", "sk-prop-scalar-six", "thm-pod-derived-poincare-duality", "sk-rem-pd-integral-corrections"]
+++
By [sk-lem-finite], $P=R\Gamma_c(X,K)$ is a perfect complex over
$\mathcal O_E$, and so is $Q=R\Gamma(X,K^\vee(d))$. By [sk-prop-scalar-six],
reduction modulo $\pi_E^n$ commutes with $R\Gamma_c$, with $R\Gamma$ and with
internal Hom, so

$$
P\otimes^L_{\mathcal O_E}A_{E,n}\simeq R\Gamma_c(X,K_n),\qquad
Q\otimes^L_{\mathcal O_E}A_{E,n}\simeq R\Gamma(X,K_n^\vee(d)),
$$

naturally in $K$. Represent $P$ by a bounded complex $P^\bullet$ of finite
free $\mathcal O_E$-modules. Its terms are torsion-free, so
$P\otimes^L_{\mathcal O_E}A_{E,n}$ is represented by $P^\bullet/\pi_E^n$, and
the short exact sequence of complexes
$0\to P^\bullet\xrightarrow{\pi_E^n}P^\bullet\to P^\bullet/\pi_E^n\to0$ gives
the long exact sequence

$$
\cdots\to H^i(P)\xrightarrow{\pi_E^n}H^i(P)\to H^i(P\otimes^L A_{E,n})
\to H^{i+1}(P)\xrightarrow{\pi_E^n}H^{i+1}(P)\to\cdots.
$$

Its cokernel and kernel terms are $H^i(P)\otimes_{\mathcal O_E}A_{E,n}$ and
the $\pi_E^n$-torsion of $H^{i+1}(P)$, which is
$\operatorname{Tor}_1^{\mathcal O_E}(H^{i+1}(P),A_{E,n})$. This is the
displayed sequence. The same argument for $Q$, and naturality of the long
exact sequence for the adjoint map $P^\vee\to Q[2d]$ of
[thm-pod-derived-poincare-duality], give the other sequences.

If the cohomology modules of $P$ are finite projective, the Tor terms vanish,
so the cohomology of $K_n$ is the reduction of the cohomology of $K$. Moreover
the $\operatorname{Ext}^1$ terms of the universal-coefficient sequence of
[sk-rem-pd-integral-corrections] vanish, so
$H^{-i}(P^\vee)=\operatorname{Hom}_{\mathcal O_E}(H^i(P),\mathcal O_E)$. The
derived pairing is perfect by [thm-pod-derived-poincare-duality], hence the
degreewise pairings are perfect $\mathcal O_E$-module pairings, and their
reductions are the corresponding pairings for $K_n$.
