+++
id = "prose-11-14"
kind = "hidden"
title = "Trace classes and local terms (4)"
order = 923
+++
In the first arrow we use the ordinary unit together with
$Rc_{2*}=Rc_{2!}$, which holds since $c_2$ is proper, and the displayed
isomorphism comes from the composition of [direct images with compact support](@proposition-construction-independence-rf-shriek).

The [Lefschetz–Verdier formula](@theorem-proper-pushforward-lefschetz-verdier) computes the trace of [$T_c(u)$](@definition-action-correspondence) in terms of
the [trace class](@definition-trace-class-local-terms). We obtain it as the special case, for the map to a point, of the
compatibility of [trace classes](@definition-trace-class-local-terms) with proper pushforward. This works because [$T_c(u)$](@definition-action-correspondence) is itself a [cohomological correspondence](@definition-correspondence): for
proper $X$ and $C$ it is a [correspondence](@definition-correspondence) on the point with coefficients
$R\Gamma(X,K)$, and on the point the [trace class](@definition-trace-class-local-terms) is the trace by
Lemma [lemma-local-terms-point]. The global trace is therefore the [trace
class](@definition-trace-class-local-terms) of a pushed-forward [correspondence](@definition-correspondence), and it remains to
show that [trace classes](@definition-trace-class-local-terms) commute with pushforward along proper maps.

To push a [cohomological correspondence](@definition-correspondence) forward along proper morphisms,
we must produce from $u$ a map
$c_2'^*Rf_*K\to c_1'^!Rf_*K$. The only maps available for this are the units and counits of the adjunctions on the two legs, used as in the
construction of [$T_c(u)$](@definition-action-correspondence). Here properness of $f$ and $g$ gives $Rf_*=Rf_!$ and $Rg_*=Rg_!$, and this allows us to push forward the
counit for $Rc_{1!}\dashv c_1^!$. We also push forward along closed immersions
(Section [sec-Additivity-of-trace-classes]).
