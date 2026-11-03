+++
kind  = "proof"
of    = "det-prop-sf-biduality-general"
+++
As in Deligne, *SGA $4\frac12$*, Ch. 5 (Dualité) 1.1–1.2 and Ch. 7
(Théorèmes de finitude) 4.1–4.6: locality, a finite smooth
stratification, the locally-free case on a stratum, and the restriction to a
stratum; the algebraic half of the coefficient hypothesis is coefficient
biduality at a geometric point, which holds stage by stage for different
reasons: at a finite stage $A$, an arbitrary finite commutative $\ell$-primary
ring, one uses biduality of perfect complexes over $A$ (the stalks of a
$D^b_{\mathrm{ctf}}$ complex are perfect), and self-injectivity of $A$ is
neither available nor needed; at the integral stage
$\mathcal O_E$ is *not* quasi-Frobenius — for
$M=\mathcal O_E/(\pi_E)$ one has $\operatorname{Hom}(M,\mathcal O_E)=0$,
so $M^{**}=0\neq M$ although $M$ is perfect — and one uses instead derived
duality of perfect complexes, $\RHom_{\mathcal O_E}(M,\mathcal O_E)\simeq M[-1]$ and $\RHom(\RHom(M,\mathcal O_E),\mathcal O_E)\simeq M$, the
$\operatorname{Ext}^1$ term being essential
([0656](https://stacks.math.columbia.edu/tag/0656),
[07VI](https://stacks.math.columbia.edu/tag/07VI): every bounded complex with
finite cohomology over the regular ring $\mathcal O_E$ is perfect, and derived
evaluation is an isomorphism for every perfect complex); at the field stages
$E$, $\Qlb$ it is vector-space duality (lem-weil-coefficient-frobenius,
rem-weil-biduality-coefficients). The derived-complete integral stage and the field
stages are reached from it by the coefficient transports
thm-coef-integral-verdier, thm-coef-rational-verdier, thm-coef-qbar-verdier.
