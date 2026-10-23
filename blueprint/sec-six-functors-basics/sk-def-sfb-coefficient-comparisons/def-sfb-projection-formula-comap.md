+++
id = "def-sfb-projection-formula-comap"
kind = "definition"
title = "Restriction of scalars and linearized functors"
order = 2606
uses = ["det-def-sfb-transport", "det-def-sfb-change-of-scalars"]
lean = ["CategoryTheory.Functor.ProjectionFormula.mapModLeftComapIso"]
+++
Let $S\colon\mathcal D\to\mathcal C$ be a strong monoidal functor and $P\colon\mathcal C\to
\mathcal D$ a functor with a projection formula $P(SL\otimes M)\cong L\otimes PM$, so that $P$
linearizes to $P_B\colon\Mod_{SB}(\mathcal C)\to\Mod_B(\mathcal D)$ for every monoid object $B$
of $\mathcal D$ ([det-def-sfb-transport]). For a morphism of monoid objects
$\varphi\colon B\to B'$ there is a natural isomorphism

$$
\operatorname{Res}_\varphi\circ P_{B'}\;\cong\;P_B\circ\operatorname{Res}_{S\varphi}\colon
\Mod_{SB'}(\mathcal C)\longrightarrow\Mod_B(\mathcal D),
$$

the identity on underlying objects.
