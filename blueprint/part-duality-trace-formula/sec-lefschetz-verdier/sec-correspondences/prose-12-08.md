+++
id = "prose-12-08"
kind = "hidden"
title = "Correspondences"
order = 547
+++
The global side of the trace formula is the trace of the endomorphism
of $R\Gamma_c(X,K)$ induced by the graph of Frobenius. The
Lefschetz–Verdier formula computes such traces for an arbitrary
correspondence, as a sum of local terms at its fixed points.

A pair of maps $c_1,c_2:C\to X$ should act on $R\Gamma_c(X,K)$ by
pulling back along $c_2$ and pushing forward along $c_1$, as a
correspondence acts on cohomology in topology. Pullback
$R\Gamma_c(X,K)\to R\Gamma_c(C,c_2^*K)$ exists when $c_2$ is proper.
Pushing forward needs a map $Rc_{1!}L\to K$ for the complex $L$ on $C$
that we have reached, and the adjunction $Rc_{1!}\dashv c_1^!$ provides
one exactly when $L=c_1^!K$, through the counit. The datum that connects
the two steps is therefore a map $u:c_2^*K\to c_1^!K$, and the resulting
endomorphism $T_c(u)$ is defined after Definition [sk-d-trace-class].
With $c_1^*$ in place of $c_1^!$ the second step fails in general. For
the inclusion $i$ of a rational point $y$ into a smooth curve $X$,

$$
\operatorname{Hom}(i_*i^*\Lambda_X,\Lambda_X)
=\operatorname{Hom}(\Lambda_y,i^!\Lambda_X)
=\operatorname{Hom}(\Lambda_y,\Lambda_y(-1)[-2])=0,
$$

so the only map $Ri_!i^*\Lambda_X\to\Lambda_X$ is zero. When $c_1$ is finite étale, smooth purity gives
$c_1^!=c_1^*$ and the counit is summation over the fibres, so $T_c(u)$
is pullback along $c_2$ followed by a sum over the fibres of $c_1$, the
shape of a Hecke operator. The Lefschetz–Verdier formula
(Theorem [sk-p-proper]) is stated in this generality,
and the trace formula applies it to the graph of Frobenius
(Definition [sk-d-weil]).

A *correspondence* on $X$ is a morphism of $k$-schemes
$c=(c_1,c_2):C\to X\times_sX$, and a *cohomological
correspondence* on $(X,K)$, for $K\in D^b_{\mathrm{ctf}}(X,A)$, is a morphism

$$
u:c_2^*K\longrightarrow c_1^!K.
$$

Here $c_2$ is the leg along which $K$ is pulled back and $c_1$ is the
leg along which we take $c_1^!$; in [sga5, III, §3] the two names are
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
