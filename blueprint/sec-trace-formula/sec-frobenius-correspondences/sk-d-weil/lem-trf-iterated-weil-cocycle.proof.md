+++
kind  = "proof"
of    = "lem-trf-iterated-weil-cocycle"
+++
By [def-trf-strict-weil-complex], $\varphi$ is an isomorphism
$Lg_\gamma^*K\to K$ with $K\in D^b_{ctf}(X,A)$; by
[def-trf-scheme-frobenius], $g_\gamma$ is an automorphism of
$X$ satisfying $g_\gamma^{m+n}=g_\gamma^m\circ g_\gamma^n$, so that
the derived pullbacks satisfy $Lg_\gamma^{m+n*}\cong Lg_\gamma^{m*}Lg_\gamma^{n*}$ under the canonical identification
displayed in the statement. Under this identification both sides of
the identity are the composite of the $m+n$ maps

$$
Lg_\gamma^{m+n*}K\xrightarrow{Lg_\gamma^{m+n-1*}\varphi}\cdots
\xrightarrow{Lg_\gamma^*\varphi}K
$$

of [def-trf-strict-weil-complex]: the left-hand side is the
composite defining $\varphi^{[m+n]}$ in
[def-trf-iterated-weil-map], while the right-hand side is the
concatenation of the composites defining $\varphi^{[m]}$ and
$\varphi^{[n]}$ in [def-trf-iterated-weil-map]; the
concatenation is identified with the composite of the $m+n$ maps by
the associativity of composition and the naturality of the canonical
pullback identifications.
