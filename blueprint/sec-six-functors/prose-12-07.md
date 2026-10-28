+++
id = "prose-12-07"
kind = "hidden"
title = "Correspondences, fixed loci and Künneth formulas"
order = 3434
+++
The global side of the trace formula is the trace of the endomorphism
of $R\Gamma_c(X,K)$ induced by the graph of Frobenius. The
Lefschetz–Verdier formula computes such traces for an arbitrary
correspondence, as a sum of local terms at its fixed points.

A *correspondence* on $X$ is a morphism of $k$-schemes
$c=(c_1,c_2):C\to X\times_sX$, and a *cohomological
correspondence* on $(X,K)$, for $K\in\Dctf(X,A)$, is a morphism

$$
u:c_2^*K\longrightarrow c_1^!K.
$$

Here $c_2$ is the leg along which $K$ is pulled back and $c_1$ is the
leg along which we take $c_1^!$; in (SGA5, III, §3) the two names are
interchanged. The *fixed locus* of $c$ is the closed subscheme

$$
\Fix(c)=C\times_{X\times X,\Delta_X}X,
 \qquad i_c:\Fix(c)\longrightarrow C,\quad d_c:\Fix(c)\longrightarrow X,
$$

where $i_c$ and $d_c$ are the two projections. Since $X$ is separated,
$\Delta_X$ and $i_c$ are closed immersions.

The example to keep in mind is the graph of an endomorphism
$\varphi:X\to X$, that is, $C=X$ with $c_1=\operatorname{id}_X$ and
$c_2=\varphi$. Then $c_1^!K=K$, a cohomological correspondence is a
morphism $u:\varphi^*K\to K$, and $\Fix(c)$ is the fixed point scheme of
$\varphi$, which we also denote $\Fix(\varphi)$. For the Frobenius $\Phi_X$ and a Weil complex this is the
correspondence whose trace formula we want.

The trace class is built from the external tensor product
$M\boxtimes N=p_1^*M\otimes^{\mathbf L} p_2^*N$ in $D((X\times X)_{\mathrm{pro\acute et}},A)$, where
$p_1,p_2:X\times X\to X$ are the projections. Its construction
uses the Künneth formula for ordinary direct images
(Proposition [sk-lem-sf-kunneth-star]) and the corresponding
formula for Verdier duals (Lemma [sk-thm-sf-kunneth-verdier]). For an ordinary direct image along one
factor, the Künneth formula is a statement about base change
(TFBP+).
