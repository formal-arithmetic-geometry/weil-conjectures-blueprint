+++
id = "det-curve-affine-artin-schreier-les"
kind = "lemma"
title = "Artin–Schreier cohomology of an affine scheme"
uses = ["lem-sc-as-sequence", "lem-sc-etale-affine-qcoherent", "def-sc-etale-qcoherent-module"]
+++
Let $U=\operatorname{Spec}A$ be an affine scheme over a field of
characteristic $p>0$ (for instance an affine curve over an algebraically
closed field of characteristic $p$), and let $\wp=F-1:A\to A$,
$\wp(a)=a^p-a$. Then the Artin–Schreier sequence induces

$$
H^0(U_{\mathrm{ét}},\mathbf F_p)=\ker(\wp:A\to A),\qquad
H^1(U_{\mathrm{ét}},\mathbf F_p)\xrightarrow{\sim}A/\wp(A),\qquad
H^q(U_{\mathrm{ét}},\mathbf F_p)=0\quad(q\geq2).
$$

The isomorphism in degree one sends the class of $a\in A$ to the class of
the $\mathbf F_p$-torsor of étale local solutions of $y^p-y=a$, and it is
natural for morphisms of affine schemes over $\mathbf F_p$.
