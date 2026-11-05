+++
kind = "proof"
of = "theorem-bounded-below-cohomology-comparison--2"
order = 123005
uses = ["proposition-comparison-morphism-inverse-image", "theorem-bounded-below-cohomology-comparison--1"]
+++
Write $\eta_M:M\to R\nu_{X,*}\nu_X^*M$ for the unit. It is invertible by
[theorem-bounded-below-cohomology-comparison--1]. Compose the two bijections

$$
\operatorname{Hom}(K,M)
\xrightarrow{\ \eta_M\circ-\ }
\operatorname{Hom}(K,R\nu_{X,*}\nu_X^*M)
\simeq\operatorname{Hom}(\nu_X^*K,\nu_X^*M).
$$

The second is the derived adjunction bijection. Its counit formula and the
triangle identity identify the composite with $f\mapsto\nu_X^*f$.
Only $M$ needs to be bounded below. Exactness of $\nu_X^*$ ensures that
it carries bounded below objects to bounded below objects, so the
restriction to $D^+$ is fully faithful.
