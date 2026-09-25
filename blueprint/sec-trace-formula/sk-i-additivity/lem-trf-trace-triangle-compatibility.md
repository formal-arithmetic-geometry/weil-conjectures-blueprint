+++
id = "lem-trf-trace-triangle-compatibility"
kind = "lemma"
title = "Triangle compatibility of the trace class"
order = 2491
uses = ["def-trf-correspondence", "def-trf-dualizing-complex", "def-trf-supported-pairing", "def-trf-trace-class", "def-trf-trace-class-source", "def-weil-derived-pullback-tensor-hom", "lem-kun-stalk-faithful-derived", "lem-trf-global-operator-triangulated", "prop-trf-pairing-point-normalization", "prop-trf-trace-formal-laws", "thm-trf-dualizing-complex-composition", "thm-trf-fixed-point-evaluation-finite", "thm-trf-kunneth-verdier"]
+++
Let $K'\to K\to K''\to K'[1]$ be a distinguished triangle in
$D^b_{ctf}(X,A)$ and let $(u',u,u'')$ be a morphism of the
corresponding triangles of the functors $Lc_2^*$ and $Rc_1^!$, so
that $\widetilde u\mapsto(\widetilde u',\widetilde u'')$ under the
induced maps of trace-class sources and $u,u',u''$ correspond under
the mate bijections of [def-trf-trace-class-source]. Then the
Verdier trace classes of [def-trf-trace-class] satisfy

$$
\operatorname{Tr}_c(u)=\operatorname{Tr}_c(u')+\operatorname{Tr}_c(u'')
$$

in $\operatorname{Hom}_{D(F,A)}(A_F,\omega_{F,A})$.
This is the additivity of the Verdier trace class; the proof below reduces
it to the point normalization of the supported pairing, so that no
filtered construction is needed. (*Source:* SGA 5, Exposé III,
4.2 and [Varshavsky,
Lefschetz–Verdier trace formula and a generalization of a theorem of
Fujiwara](https://arxiv.org/pdf/math/0505564), Section 5; the argument below is the blueprint-internal one.)

## Proof

By [def-trf-supported-pairing] the trace class is the supported
pairing $\operatorname{Tr}_c(u)=\langle u,1_K\rangle_{\mathrm{LV}}$; by [def-trf-trace-class] it is also
the composite of the mate $\widetilde u$ of
[def-trf-correspondence] with the trace map
$\mathfrak t_{c,K}$. Both descriptions produce an element of
$\operatorname{Hom}_{D(F,A)}(A_F,\omega_{F,A})$, and both are natural
in the coefficient: the ingredients of the pairing recipe are the
Kunneth–Verdier isomorphisms
[thm-trf-kunneth-verdier], the projection formula and
$!$-base change, the Verdier evaluations and the exceptional
adjunctions, all of which are compatible with pullback by
[def-weil-derived-pullback-tensor-hom].

*Step 1 (reduction to the geometric points of $F$).* A morphism
of complexes of $A_F$-modules vanishes if and only if all its
pullbacks to geometric points vanish, by
[lem-kun-stalk-faithful-derived]. For a geometric point
$\bar y\to F$, the pullback of the dualizing complex is the dualizing
complex of the point, $A$ in degree $0$, by the composition
property [thm-trf-dualizing-complex-composition] applied to the
morphism $\Spec\kappa(\bar y)\to F$, since a point has dualizing
complex $A$ ([def-trf-dualizing-complex]). Hence it suffices to
prove

$$
Li_{\bar y}^*\operatorname{Tr}_c(u)
=Li_{\bar y}^*\operatorname{Tr}_c(u')
+Li_{\bar y}^*\operatorname{Tr}_c(u'')
\qquad\text{in }A
$$

for every geometric point $\bar y$ of $F$.

*Step 2 (the restriction at a point is a categorical trace).* At
$\bar y$ the correspondence has support the point $\bar y$, so its
two legs induce the two maps between the stalks which constitute the
correspondence data of the point, and the recipe of
[def-trf-supported-pairing] is built from operations which are
natural in the coefficient; hence the restriction of the pairing to
$\bar y$ is the supported pairing of the restricted data. By the
point normalization
[prop-trf-pairing-point-normalization] that pairing is the
categorical trace $\operatorname{tr}_A(v_{\bar y}u_{\bar y}\mid P)$;
for the trace class one takes $v=1_K$, and the value of the stalk
trace is $\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y})$, as computed
in [thm-trf-fixed-point-evaluation-finite]. Thus

$$
Li_{\bar y}^*\operatorname{Tr}_c(u)
=\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y}),
$$

and likewise for $u'$ and $u''$.

*Step 3 (additivity of the three stalk traces).* Pullback to the
geometric point is exact, so the restrictions
$K'_{\bar y}\to K_{\bar y}\to K''_{\bar y}\to K'_{\bar y}[1]$ again form a distinguished triangle, and the
compatibility hypothesis on $(u',u,u'')$ is preserved by the
naturality of the pullback functors; consequently the three
endomorphisms $u'_{\bar y},u_{\bar y},u''_{\bar y}$ form an
endomorphism of this triangle, exactly as in
[lem-trf-global-operator-triangulated] after restriction to the
point. Triangle additivity of the categorical trace
[prop-trf-trace-formal-laws](2) therefore gives

$$
\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y})
=\operatorname{tr}_A(u'_{\bar y}\mid K'_{\bar y})
+\operatorname{tr}_A(u''_{\bar y}\mid K''_{\bar y}).
$$

*Conclusion.* Combining Steps 2 and 3, the pullbacks of
$\operatorname{Tr}_c(u)$ and of
$\operatorname{Tr}_c(u')+\operatorname{Tr}_c(u'')$ to every geometric
point of $F$ agree; by Step 1 the two classes are equal, which is the
assertion.
