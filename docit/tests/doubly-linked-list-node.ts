/*
 *	Created by Trevor Sears <trevorsears.main@gmail.com>.
 *	12:54 PM -- March 14th, 2019.
 *	Project: @jsdsl/doubly-linked-list
 */

import { DoublyLinkedList } from "./doubly-linked-list";
import { IDoublyLinkedListNode } from "./i-doubly-linked-list-node";

/**
 * A doubly-linked node within a {@link DoublyLinkedList}.
 *
 * @author Trevor Sears <trevorsears.main@gmail.com>
 * @version v0.2.0
 * @since v0.1.0
 */
export class DoublyLinkedListNode<E> implements IDoublyLinkedListNode<E> {

	/**
	 * A reference to the node preceding this node, or undefined if this node has no preceding sibling.
	 */
	private previous: DoublyLinkedListNode<E> | undefined;

	/**
	 * A reference to the node succeeding this node, or undefined if this node has no successive sibling.
	 */
	private next: DoublyLinkedListNode<E> | undefined;

	/**
	 * A reference to the {@link DoublyLinkedList} to which this node belongs.
	 */
	private parentList: DoublyLinkedList<E>;

	/**
	 * The content that this node contains.
	 *
	 * This will always be null for the prologue and epilogue nodes in any given {@link DoublyLinkedList}.
	 */
	private content: E | null;

	/**
	 * Initializes a new DoublyLinkedListNode with the provided contents, parent list, and optional preceding and
	 * successive nodes.
	 *
	 * @param content The content to initialize this node with.
	 * @param parentList The {@link DoublyLinkedList} that contains this node.
	 * @param previousNode The node that should be set as this node's preceding sibling.
	 * @param nextNode The node that should be set as this node's successive sibling.
	 */
	public constructor(content: E | null, parentList: DoublyLinkedList<E>, previousNode?: DoublyLinkedListNode<E>,
					   nextNode?: DoublyLinkedListNode<E>) {

		this.content = content;
		this.parentList = parentList;
		this.previous = previousNode;
		this.next = nextNode;

	}

	public getElement(): E {

		if (this.content !== null) return this.content;
		else {

			let name: string = (this.hasPreviousNode() ? "epilogue" : "prologue");

			throw new Error("ERR | Attempted to retrieve null content out of a DoublyLinkedListNode (" + name +
				" node).");

		}

	}

	public getParentList(): DoublyLinkedList<E> {

		return this.parentList;

	}

	public hasPreviousNode(): boolean {

		return (this.previous !== undefined);

	}

	public getPreviousNode(): DoublyLinkedListNode<E> | undefined {

		if (!this.hasPreviousNode()) return undefined;
		else return this.previous as DoublyLinkedListNode<E>;

	}

	public setPreviousNode(previousNode: DoublyLinkedListNode<E> | undefined): DoublyLinkedListNode<E> | undefined {

		let displaced: DoublyLinkedListNode<E> | undefined = this.previous;
		this.previous = previousNode;
		return displaced;

	}

	public hasNextNode(): boolean {

		return (this.next !== undefined);

	}

	public getNextNode(): DoublyLinkedListNode<E> | undefined {

		if (!this.hasNextNode()) return undefined;
		else return this.next as DoublyLinkedListNode<E>;

	}

	public setNextNode(nextNode: DoublyLinkedListNode<E> | undefined): DoublyLinkedListNode<E> | undefined {

		let displaced: DoublyLinkedListNode<E> | undefined = this.next;
		this.next = nextNode;
		return displaced;

	}

}