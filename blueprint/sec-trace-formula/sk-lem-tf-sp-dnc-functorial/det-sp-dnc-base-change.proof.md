+++
kind = "proof"
of = "det-sp-dnc-base-change"
uses = ["det-sp-dnc-definition"]
+++
(1) Since $f^{\cdot}I\subset I'$, the map $\mathcal O_X[t,t^{-1}]\to f_*\mathcal O_{X'}[t,t^{-1}]$
sends $a/t$ to $f^{\cdot}(a)/t\in\mathcal O_{X'}[t,I'/t]$, so it restricts to a map of the
subalgebras of [det-sp-dnc-definition]; base change to $S$ gives $\widetilde f$.

(2) If $I'=I\mathcal O_{X'}$, the natural map

$$
f^{*}\mathcal O_X[t,I/t]\longrightarrow\mathcal O_{X'}[t,I'/t]
$$

from the base-changed Rees algebra is surjective, because both sides are generated over
$\mathcal O_{X'}[t]$ by the images of the $a/t$, $a\in I$. This is the closed immersion. If $f$ is
flat, then $f^*$ preserves the inclusions $I^r\subset\mathcal O_X$ and $I^r\mathcal O_{X'}=I'^r$,
so the map is injective after flat base change, hence an isomorphism. On the associated graded
algebras, modulo $t$, the positive-degree generators of $\operatorname{gr}_I$ generate the
positive-degree ideal of $\operatorname{gr}_{I'}$. Killing them gives $\mathcal O_{Z'}$, which
proves $\widetilde f_s^{-1}(Z)=Z'$.

(3) If $f$ is proper, $\widetilde f$ is the closed immersion of (2) followed by the base change
$X'\times_X\mathcal D_ZX\to\mathcal D_ZX$ of $f$, which is proper. If $f$ is smooth, it is flat, so
by (2) $\widetilde f$ is the base change of $f$, hence smooth.
