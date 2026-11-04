+++
id = "prose-09-07"
kind = "hidden"
title = "Reduction to constant coefficients on a curve"
order = 403
+++
Assume now that $q\geq1$ and that $\mathrm{BC}(g,n,q-1)$ holds. If
$\mathrm{BC}(g,n,q)$ fails, the next four lemmas, all on the étale
sites, reduce us to a failure with constant coefficients and direct image from
the spectrum of an algebraically closed field, in the form of
Lemma [sk-lem-universal-datum]. A failure persists under these changes
because the base change map is injective in degree $q$.

The argument is by contradiction rather than by dévissage, and
injectivity is what makes this possible. An isomorphism cannot be
transported along an embedding $M\hookrightarrow N$, but a nonzero cokernel
can: by Lemma [sk-prop-injectivity] the cokernel for $M$ embeds into the
cokernel for $N$. So we may replace the coefficient sheaf by a larger one,
the source of the direct image by a closed subscheme or an open subscheme
carrying the failure, and finally by its generic point, the spectrum of a
field (Lemma [sk-lem-failure-field]). Integral morphisms have exact
direct images, so the failure also survives integral changes of the source
and of the base (Lemma [sk-lem-sbc-integral-tests]). After these moves the
direct image is from $\operatorname{Spec}\Omega$ with $\Omega$
algebraically closed, whose cohomology vanishes in positive degrees, and
the whole failure is concentrated in $R^qh_*\mathbf Z/m$ for the
extension of the ground field from $L$ to $\Omega$ along a smooth curve.
This is the geometric heart of the theorem, and it comes down to the
invariance of $H^1$ of curves under extension of algebraically closed
fields.
