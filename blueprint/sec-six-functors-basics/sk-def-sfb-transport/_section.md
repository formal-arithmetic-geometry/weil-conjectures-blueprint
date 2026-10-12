+++
id = "sk-def-sfb-transport"
kind = "definition"
title = "Transport of module objects and projection formulas"
order = 1580
uses = ["sk-def-sfb-change-of-scalars"]
lean = ["CategoryTheory.Functor.mapMod", "CategoryTheory.Adjunction.mapModAdjunction", "CategoryTheory.Functor.ProjectionFormula", "CategoryTheory.Functor.ProjectionFormula.mapModLeft", "CategoryTheory.Functor.ProjectionFormula.mapModRight", "CategoryTheory.Functor.ProjectionFormula.mapModAdjunction", "CategoryTheory.Adjunction.HasProjectionFormula", "CategoryTheory.Adjunction.projectionFormula", "CategoryTheory.Adjunction.mapModLeftAdjunction"]
tags = ["sketch"]
+++
Let $\mathcal C$ and $\mathcal D$ be monoidal categories. Monoid objects and module objects
are as in [sk-def-sfb-ring-object] and [sk-def-sfb-module-objects].

1. **Transport along a lax monoidal functor.** Let $F\colon\mathcal C\to\mathcal D$ be lax
   monoidal, with structure maps $\mu^F_{X,Y}\colon FX\otimes FY\to F(X\otimes Y)$. For a
   monoid object $\mathcal R$ of $\mathcal C$, $F\mathcal R$ is a monoid object of
   $\mathcal D$. An $\mathcal R$-module object $M$ gives the $F\mathcal R$-module object
   $FM$, with action
   $F\mathcal R\otimes FM\xrightarrow{\mu^F}F(\mathcal R\otimes M)\xrightarrow{F\gamma_M}FM$.
   This defines a functor
   $$
   \operatorname{mapMod}(F)\colon\Mod_{\mathcal R}(\mathcal C)\to\Mod_{F\mathcal R}(\mathcal D)
   $$
   that commutes with the forgetful functors.
2. **Monoidal adjunctions.** Let $F\dashv G$ be a monoidal adjunction, with $F$ strong
   monoidal and $G$ lax monoidal, the structures being mates. Then the unit
   $u_{\mathcal R}\colon\mathcal R\to GF\mathcal R$ is a morphism of monoid objects, and,
   with the restriction of scalars of [sk-def-sfb-change-of-scalars],
   $$
   \operatorname{mapMod}(F)\dashv\operatorname{Res}_{u_{\mathcal R}}\circ\operatorname{mapMod}(G).
   $$
3. **Projection formulas.** Let $S\colon\mathcal D\to\mathcal C$ be strong monoidal and
   $P\colon\mathcal C\to\mathcal D$ a functor. A *projection formula* for $P$ relative to
   $S$ is a family of isomorphisms $P(SL\otimes M)\cong L\otimes PM$, natural in $L$ and
   $M$ and compatible with the unit and the associativity constraints. It *linearizes*
   $P$: for every monoid object $\mathcal B$ of $\mathcal D$, it gives a functor
   $$
   P_{\mathcal B}\colon\Mod_{S\mathcal B}(\mathcal C)\to\Mod_{\mathcal B}(\mathcal D),
   \qquad M\mapsto PM,
   $$
   where $\mathcal B$ acts by
   $\mathcal B\otimes PM\cong P(S\mathcal B\otimes M)\xrightarrow{P\gamma_M}PM$. Every
   right adjoint $G$ of $P$ linearizes to a functor
   $G_{\mathcal B}\colon\Mod_{\mathcal B}(\mathcal D)\to\Mod_{S\mathcal B}(\mathcal C)$,
   $N\mapsto GN$, and $P_{\mathcal B}\dashv G_{\mathcal B}$.
4. **Adjunctions $P\dashv S$.** For an adjunction $P\dashv S$ with $S$ strong monoidal, the
   *projection formula map* $P(SL\otimes M)\to L\otimes PM$ is the adjoint of
   $SL\otimes M\to SL\otimes SPM\to S(L\otimes PM)$. If these maps are isomorphisms, they
   form a projection formula. Then $G_{\mathcal B}=\operatorname{mapMod}(S)$, so
   $P_{\mathcal B}\dashv\operatorname{mapMod}(S)$.
