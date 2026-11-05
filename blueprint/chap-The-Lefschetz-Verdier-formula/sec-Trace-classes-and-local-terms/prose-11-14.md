+++
id = "prose-11-14"
kind = "hidden"
title = "Trace classes and local terms (4)"
order = 923
+++
In the first arrow we use the ordinary unit together with
$Rc_{2*}=Rc_{2!}$, which holds since $c_2$ is proper, and the displayed
isomorphism comes from the composition of direct images with compact support.

The Lefschetz–Verdier formula computes the trace of $T_c(u)$ in terms of
the trace class. We obtain it as the special case, for the map to a point, of the
compatibility of trace classes with proper pushforward. This works because $T_c(u)$ is itself a cohomological correspondence: for
proper $X$ and $C$ it is a correspondence on the point with coefficients
$R\Gamma(X,K)$, and on the point the trace class is the trace by
Lemma [lemma-local-terms-point]. The global trace is therefore the trace
class of a pushed-forward correspondence, and it remains to
show that trace classes commute with pushforward along proper maps.

To push a cohomological correspondence forward along proper morphisms,
we must produce from $u$ a map
$c_2'^*Rf_*K\to c_1'^!Rf_*K$. The only maps available for this are the units and counits of the adjunctions on the two legs, used as in the
construction of $T_c(u)$. Here properness of $f$ and $g$ gives $Rf_*=Rf_!$ and $Rg_*=Rg_!$, and this allows us to push forward the
counit for $Rc_{1!}\dashv c_1^!$. We also push forward along closed immersions
(Section [sec-Additivity-of-trace-classes]).
