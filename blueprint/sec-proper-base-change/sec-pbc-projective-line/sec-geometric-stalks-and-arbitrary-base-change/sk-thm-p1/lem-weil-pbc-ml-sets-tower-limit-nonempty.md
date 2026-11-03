+++
id = "lem-weil-pbc-ml-sets-tower-limit-nonempty"
kind = "lemma"
title = "A Mittag-Leffler tower of nonempty sets has a nonempty limit (Stacks 0597, index set the positive integers)"
lean = ["CategoryTheory.Functor.nonempty_sections_of_isMittagLeffler"]
order = 1992
+++
Let $(E_i,f_i)_{i\ge1}$ be an inverse system of sets (sets $E_i$ and maps $f_i:E_{i+1}\to E_i$), with composites $\varphi_{k,i}=f_i\circ f_{i+1}\circ\cdots\circ f_{k-1}:E_k\to E_i$ for $k\ge i$ ($\varphi_{i,i}=\mathrm{id}$). Assume that every $E_i$ is nonempty and that $(E_i)$ satisfies the Mittag-Leffler condition: for every $i\ge1$ there is an integer $c(i)\ge i$ such that $\varphi_{k,i}(E_k)=\varphi_{c(i),i}(E_{c(i)})$ (as subsets of $E_i$) for all $k\ge c(i)$. Then the limit $\varprojlim_iE_i=\{(x_i)_{i\ge1}\in\prod_{i\ge1}E_i: f_i(x_{i+1})=x_i\text{ for all }i\ge1\}$ is nonempty.
