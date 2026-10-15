+++
id = "sk-thm-groth-ss"
kind = "theorem"
title = "Grothendieck spectral sequence and its Leray specialization"
order = 716
uses = ["sk-def-groth-ss"]
lean = ["CategoryTheory.Functor.exists_grothendieckSpectralSequence"]
tags = ["sketch"]
+++
Let $\mathcal A,\mathcal B$ be Grothendieck abelian categories,
$\mathcal C$ an abelian category, and $\Phi:\mathcal A\to\mathcal B$,
$\Psi:\mathcal B\to\mathcal C$ additive left exact functors forming a
composable pair with acyclicity in the sense of [sk-def-groth-ss]
($\Phi$ sends injective objects to $\Psi$-acyclic objects). Then for
every $A\in\mathcal A$ there is a first-quadrant cohomological spectral
sequence

$$
E_2^{p,q}\cong R^p\Psi\bigl(R^q\Phi(A)\bigr)\ \Longrightarrow\ R^{p+q}(\Psi\circ\Phi)(A).
$$

In particular, let $X\xrightarrow{f}Y\xrightarrow{h}Z$ be morphisms of sites (or
schemes with their étale or small Zariski sites). For an abelian
sheaf $F$ on $X$, since $f_*$ carries injectives
to $h_*$-acyclics ($f_*$ is right adjoint to the exact $f^{-1}$, so
it preserves injectives), there is a spectral sequence

$$
E_2^{p,q}=R^ph_*R^qf_*F\ \Longrightarrow\ R^{p+q}(hf)_*F.
$$

For $Z$ the punctual site, so that $h_*=\Gamma(Y,-)$, this is the
*Leray* spectral sequence

$$
E_2^{p,q}=H^p(Y,R^qf_*F)\ \Longrightarrow\ H^{p+q}(X,F).
$$

In particular this includes $Y_{\mathrm{zar}}$ and $X_{\mathrm{zar}}$
for a morphism of schemes. For proper $f$ and coherent $F$ the
Zariski sequence is the spectral sequence of
$\Gamma(Y,-)\circ f_*$ on $\cO$-modules.
