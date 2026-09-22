+++
id = "lem-sc-kummer-les"
kind = "lemma"
title = "Consequences of the Kummer sequence"
order = 3669
lean = ["AlgebraicGeometry.Curve.shortExact_kummer_h1", "AlgebraicGeometry.Curve.h2_rootsOfUnity_eq_coker"]
uses = ["lem-sc-brauer-zero"]
+++
Let $C$ be a curve over algebraically closed $k$ and let $n$ be prime to
$\operatorname{char}k$. Assume $H^2(C_{\Et},\mathbf G_m)=0$
[lem-sc-brauer-zero]. Then, under the canonical identification of the
Picard group with $H^1(C_{\Et},\mathbf G_m)$, there is a canonical short
exact sequence
$$
 0\to\mathcal O_C(C)^\times/\mathcal O_C(C)^\times{}^{\,n}
 \to H^1(C_{\Et},\mu_n)\to\operatorname{Pic}(C)[n]\to0,
$$
and
$$
 H^2(C_{\Et},\mu_n)=\operatorname{coker}\bigl(n:
 \operatorname{Pic}(C)\to\operatorname{Pic}(C)\bigr),
$$
and $H^0(C,\mu_n)=\mu_n(k)=\mathbf Z/n\mathbf Z$. In particular
$H^1(C_{\Et},\mu_n)=\operatorname{Pic}(C)[n]$ when
$\mathcal O_C(C)^\times$ is $n$-divisible (e.g. when $C$ is proper, so
$\mathcal O_C(C)^\times=k^\times$).

## Proof

Take the long exact sequence in cohomology of the exact Kummer sequence:
$$
\begin{array}{l}
 0\to H^0(C,\mu_n)\to H^0(C,\mathbf G_m)\xrightarrow{n}
 H^0(C,\mathbf G_m)\to
 H^1(C,\mu_n)\to H^1(C,\mathbf G_m)\xrightarrow{n}\\
 \hphantom{0\to{}}
 H^1(C,\mathbf G_m)\to H^2(C,\mu_n)\to H^2(C,\mathbf G_m)\to\cdots.
\end{array}
$$
Here $H^0(C,\mathbf G_m)=\mathcal O_C(C)^\times$ and $k$ is algebraically
closed, so $x\mapsto x^n$ is surjective on the constant part
$k^\times\subseteq\mathcal O_C(C)^\times$;
$H^1(C,\mathbf G_m)=\operatorname{Pic}(C)$ by the identification of the
Picard group with the first cohomology of units; and the term
$H^2(C,\mathbf G_m)$ is zero by [lem-sc-brauer-zero]. Exactness of the
sequence at $H^1(C,\mu_n)$ and at $H^1(C,\mathbf G_m)$ therefore gives the
displayed short exact sequence and the displayed formula for
$H^2(C,\mu_n)$; the $H^0$-term is $\mu_n(k)=\mathbf Z/n\mathbf Z$ by the
primitive-root lemma. The last assertion follows because for $C$ proper and
connected the only units are the constants $k^\times$, which are
$n$-divisible since $k$ is algebraically closed.

Unresolved dependencies: def:sc-curves, def:sc-kummer-sequence, lem:sc-kummer-exact, lem:sc-h1-gm-pic, lem:sc-primitive-root
