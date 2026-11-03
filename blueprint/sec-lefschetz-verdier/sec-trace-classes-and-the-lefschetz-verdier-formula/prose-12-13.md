+++
id = "prose-12-13"
kind = "hidden"
title = "Trace classes and the Lefschetz–Verdier formula (3)"
order = 560
+++
The global side of the trace formula is the trace of the following
endomorphism. If $c_2$ is proper, $u$ acts on compactly supported
cohomology by the endomorphism

$$
\begin{aligned}
T_c(u):R\Gamma_c(X,K)&\xrightarrow{\eta_{c_2}}
R\Gamma_c(C,c_2^*K)\xrightarrow{u}R\Gamma_c(C,c_1^!K)\\
&\simeq R\Gamma_c(X,Rc_{1!}c_1^!K)
\xrightarrow{\varepsilon_{c_1}}R\Gamma_c(X,K).
\end{aligned}
$$

The first arrow uses the ordinary unit and $Rc_{2*}=Rc_{2!}$, and
the displayed isomorphism comes from the composition of direct images
with compact support.

The Lefschetz–Verdier formula computes the trace of $T_c(u)$ in terms of
the trace class. It is the special case, for the map to a point, of the
compatibility of trace classes with proper pushforward, and we first
explain how proper morphisms push cohomological correspondences forward.
The idea is that $T_c(u)$ is itself a cohomological correspondence: for
proper $X$ and $C$ it is a correspondence on the point with coefficients
$R\Gamma(X,K)$, and on the point the trace class is the trace
(Lemma [sk-p-pairing]). So the global trace is the trace
class of a pushed-forward correspondence, and the formula follows once
trace classes are shown to commute with pushforward along a proper map.
The pushforward along $f:X\to Y$ must produce a map
$c_2'^*Rf_*K\to c_1'^!Rf_*K$ from $u$, and the only maps available are
units and counits of the adjunctions on the two legs, used as in the
construction of $T_c(u)$. Properness of $f$ and $g$ is needed so that
$Rf_*=Rf_!$ and $Rg_*=Rg_!$, which lets the counit for
$Rc_{1!}\dashv c_1^!$ be pushed forward. In topology, fixed-point
classes push forward along proper maps, compatibly with Lefschetz
numbers. The definition is used again with a closed
immersion $f$, to describe the piece $u_Z$ of
Proposition [sk-i-additivity], and in the proof of
Proposition [sk-p-frob].
