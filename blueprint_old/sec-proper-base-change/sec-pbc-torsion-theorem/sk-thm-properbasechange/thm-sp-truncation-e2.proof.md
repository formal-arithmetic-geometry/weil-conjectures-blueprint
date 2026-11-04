+++
kind  = "proof"
of    = "thm-sp-truncation-e2"
+++
The exact couple of [def-sp-truncation-couple] is an exact couple by
[lem-sp-truncation-couple-exact], and it is the couple of a t-structure
("heart") filtration, so by the spectral sequence of
[def-sp-exact-couple] the $E_2$-page is $E_2^{p,q}=R^pv(\mathcal H^qK)$, the
identification of the shifted cohomology being the shift rule
[lem-sp-shift-identification]. The abutment is $\mathcal H^{p+q}(RvK)$ with
the image filtration of [def-sp-image-filtration]. The $D$-terms vanish for
$q<a$ because $\tau_{\leq q}K=0$. The functor $Rv$ is left t-exact: an object
with no cohomology below $b$ has an injective resolution in the sense of
[def-sp-injective-resolutions] starting in degree $b$, and applying the left
exact functor does not introduce lower terms. Applied to $\tau_{>n}K$, this
shows $D^{0,n}=H^n(Rv\tau_{\leq n}K)=H^n(RvK)$. The hypotheses and the
abutment identification of [thm-sp-half-plane-convergence] therefore hold. In
particular the entries stabilize for $r>\max(q-a+1,p)$, and the stated finite
filtration is the one constructed there.

For the étale special case, the first sequence is the theorem for $v=f_*$
on $\operatorname{Ab}(X_{\Et})$ ([def-sp-etale-dictionary]). The second is the
theorem for $v=f'_*$ applied to $g'^{-1}K$: the inverse image $g'^{-1}$ is
exact, so $\mathcal H^q(g'^{-1}K)=g'^{-1}\mathcal H^q(K)$, which vanishes for
$q<a$, and $g'^{-1}\tau_{\leq q}K=\tau_{\leq q}g'^{-1}K$. This gives the
displayed ${E'}_2$-page and filtration.
