+++
id = "a43-33.-densification-after-base-change"
kind = "section"
title = "A43/33. Densification after base change"
order = 1924
+++
Let $g:Y'\to Y$ be an arbitrary morphism with both $Y$ and $Y'$ noetherian
and finite-dimensional. Put $X'=X\times_Y Y'$ and

$$
\overline X_{C,g}^{\mathrm{raw}}=\overline X_C\times_Y Y'.
$$

The pulled-back open need not be dense. Define the dense model by schematic
closure

$$
\overline X_{C,g}^{\mathrm{den}}
=\overline{X'}^{\,\mathrm{sch}}
\subset\overline X_{C,g}^{\mathrm{raw}},
\qquad
d_{C,g}:\overline X_{C,g}^{\mathrm{den}}
\longrightarrow\overline X_{C,g}^{\mathrm{raw}}.
\tag{BA43-DEN}
$$

The schematic-closure leaf proves that $d_{C,g}$ is the resulting closed
proper map and that it restricts to the identity on $X'$.

**Formalization note.** The *flat* case of the base change above is formalized:
`AlgebraicGeometry.Compactification.isSchemeTheoreticallyDominant_i_ofIsPullback`
(`WeilConjectures/Compactification/BaseChange.lean`) proves that if $g$ is flat and
the quasi-compact open immersion $j_C$ is scheme-theoretically dominant, then so is the open
immersion of $\overline X_{C,g}^{\mathrm{raw}}$; that is, for flat $g$ the raw pullback is
already dense and no densification is needed. The base changed compactification itself is
`AlgebraicGeometry.Compactification.ofIsPullback`. For a general $g$ the schematic
closure (BA43-DEN) is still required and remains open; see
`GEO-BA43-SCHEMATIC-CLOSURE-DENSIFICATION`.

A raw compactification is data

$$
R=(X'\xrightarrow{j_R}\overline X_R\xrightarrow{p_R}Y',
\epsilon_R:p_R\circ j_R=f'),
\tag{BA43-RAW-DATA}
$$

with $j_R$ open and $p_R$ proper and finitely presented, but with no density
condition. Its stored equation $\epsilon_R$ is part of the type, and
$F_R^{\mathrm{amb}}=Rp_{R*}Rj_{R!}$ is a functor
$D^+(X'_{\acute et},\Lambda_n)\to D^+(Y'_{\acute et},\Lambda_n)$.
Its $D_c^+$ restriction is asserted only after a constructibility theorem.
Raw models are not objects of the dense
refinement category and have no $\kappa$ arrows.

The terminal leaf `CAT-GEO-BA43-DENSE-TO-RAW-SUPPORT` has exactly one
output:

$$
\gamma^{\mathrm{raw}}_{d_{C,g}}:
Rd_{C,g*}Rj_{C_g^{\mathrm{den}}!}
\xrightarrow{\sim}Rj_{C_g^{\mathrm{raw}}!}.
\tag{BA43-GAMMA-RAW}
$$

It outputs neither $\sigma$, nor refinement naturality, nor identity,
iterated-base-change, or open-exchange coherence. Those are all conclusions
of the middle reassembly `OBL-BA43-BASECHANGE-DENSIFICATION`. Using
proper-direct-image composition, that middle owner first defines

$$
\sigma_{C,g}:F_{C_g^{\mathrm{den}}}
\xrightarrow{\sim}F_{C_g^{\mathrm{raw}}}.
\tag{BA43-SIGMA}
$$

It must then prove the following four separately owned diagrams. For a
refinement $q:D\to C$, let $\rho^{\mathrm{den}}_{q,g}$ and
$\rho^{\mathrm{raw}}_{q,g}$ be the proper-support comparisons already
constructed by `OBL-BA43-REFINEMENT-EXCHANGE` on the densified and raw
pullbacks. Refinement naturality is the
commutative square

$$
\begin{CD}
F_{D_g^{\mathrm{den}}} @>{\sigma_{D,g}}>> F_{D_g^{\mathrm{raw}}}\\
@V{\rho^{\mathrm{den}}_{q,g}}VV @VV{\rho^{\mathrm{raw}}_{q,g}}V\\
F_{C_g^{\mathrm{den}}} @>{\sigma_{C,g}}>> F_{C_g^{\mathrm{raw}}}.
\end{CD}
\tag{BA43-DEN-REF}
$$

After the canonical identifications
$C_{\mathrm{id}}^{\mathrm{den}}=C_{\mathrm{id}}^{\mathrm{raw}}=C$, identity
coherence is the equation

$$
\sigma_{C,\mathrm{id}_Y}=1_{F_C}.
\tag{BA43-DEN-ID}
$$

For $Y''\xrightarrow{h}Y'\xrightarrow{g}Y$, let
$\delta_{C;g,h}:(C_g^{\mathrm{den}})_h^{\mathrm{den}} \xrightarrow{\sim}C_{gh}^{\mathrm{den}}$ be the canonical comparison of the
two schematic closures. Let $\tau_{C;g,h}$ be the proper-support comparison
from $(C_g^{\mathrm{den}})_h^{\mathrm{raw}}$ to $C_{gh}^{\mathrm{raw}}$
induced by the base change of $d_{C,g}$. Iterated coherence is

$$
\begin{CD}
F_{(C_g^{\mathrm{den}})_h^{\mathrm{den}}}
@>{F(\delta_{C;g,h})}>> F_{C_{gh}^{\mathrm{den}}}\\
@V{\sigma_{C_g^{\mathrm{den}},h}}VV @VV{\sigma_{C,gh}}V\\
F_{(C_g^{\mathrm{den}})_h^{\mathrm{raw}}}
@>{\tau_{C;g,h}}>> F_{C_{gh}^{\mathrm{raw}}}.
\end{CD}
\tag{BA43-DEN-ITER}
$$

Finally let
$A=L\bar g_{\mathrm{raw}}^*Rj_{C!}K$ and let
$s_d:A\xrightarrow{\sim}Rd_{C,g*}Ld_{C,g}^*A$ be the closed-support
identification. Construct the raw and dense open-exchange maps independently.
Open-exchange coherence is precisely

$$
\begin{CD}
A @>{\beta^{\mathrm{raw}}_{j_C,g,K}}>>
Rj_{C_g^{\mathrm{raw}}!}Lg'^*K\\
@V{s_d}VV @VV{(\gamma^{\mathrm{raw}}_{d_{C,g}})^{-1}}V\\
Rd_{C,g*}Ld_{C,g}^*A
@>{Rd_{C,g*}(\beta^{\mathrm{den}}_{j_C,g,K})}>>
Rd_{C,g*}Rj_{C_g^{\mathrm{den}}!}Lg'^*K.
\end{CD}
\tag{BA43-DEN-OPX}
$$

None of these equations is a field of (BA43-GAMMA-RAW).
