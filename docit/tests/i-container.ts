/*
 *	Created by Trevor Sears <trevorsears.main@gmail.com>.
 *	3:49 PM -- October 04th, 2019.
 *	Project: @jsdsl/container
 */

import { Stream, Streamable } from "@jsdsl/stream";
import { Iterator, Iterable } from "@jsdsl/iterator";

/**
 * An interface representing the general form of a data structure that contains elements.
 *
 * @author Trevor Sears <trevorsears.main@gmail.com>
 * @version v0.1.0
 * @since v0.1.0
 */
export interface IContainer<E> extends Iterable<E>, Streamable<E> {
	
	/**
	 * Returns true if and only if this IContainer contains all of the elements provided as arguments.
	 * 
	 * @param elements The elements to check this container for.
	 * @return true if and only if this IContainer contains all of the elements provided as arguments.
	 */
	contains(...elements: E[]): boolean;
	
	/**
	 * Returns the number of elements contained in this IContainer.
	 * 
	 * @return The number of elements contained in this IContainer.
	 */
	size(): number;
	
	/**
	 * Returns true if and only if this IContainer holds no elements.
	 * 
	 * @return true if and only if this IContainer holds no elements.
	 */
	isEmpty(): boolean;
	
	/**
	 * Returns an array representation of the elements contained in this IContainer.
	 * 
	 * @return An array representation of the elements contained in this IContainer.
	 */
	toArray(): E[];
	
	/**
	 * Removes all of this IContainer's elements, rendering it empty.
	 */
	clear(): void;
	
}