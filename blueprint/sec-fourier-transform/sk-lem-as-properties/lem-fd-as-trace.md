+++
id = "lem-fd-as-trace"
kind = "lemma"
title = "Trace function of the Artin–Schreier sheaf"
lean = ["AlgebraicGeometry.WeilSheaf.traceFunction_artinSchreier"]
order = 3942
uses = ["def-fd-additive-character", "def-fd-artin-schreier-sheaf", "def-weil-local-frobenius-trace", "lem-fd-as-cover-affine-line", "lem-wft-as-comparison"]
+++
Let $k_0=\mathbf F_q$, fix the nondegenerate additive character
$\psi=\Psi\circ\operatorname{Tr}_{k_0/\mathbf F_p}$ of [def-fd-additive-character],
let $a\in k_0^\times$, and let $\mathcal L_{\psi,ax}$ be the
Artin–Schreier sheaf of [def-fd-artin-schreier-sheaf] on
$\mathbf A^1_{k_0}$ attached to the linear function $x\mapsto ax$.
Then the *trace function* of $\mathcal L_{\psi,ax}$ is

$$
t_{\mathcal L_{\psi,ax}}(u)=\psi\bigl(\operatorname{Tr}_{\kappa(u)/k_0}(au)\bigr)
=\Psi\bigl(\operatorname{Tr}_{\kappa(u)/\mathbf F_p}(au)\bigr),
$$

for every closed point $u$ (with the local Frobenius convention of
[def-weil-local-frobenius-trace]); in particular, on the
$\mathbf F_{q^n}$-points of the line,

$$
t_{\mathcal L_{\psi,ax}}(x)=\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}(ax)\bigr).
$$
